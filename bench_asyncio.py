import asyncio
import json

import aioamqp
import chilero.web

import config


class Application(chilero.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)

        self._transport = None
        self._protocol = None
        self._channel = None

    @asyncio.coroutine
    def publish(self, message):
        if self._channel is None:
            yield from self.mq_connect()

        yield from self._channel.basic_publish(
            json.dumps(message), exchange_name=config.EXCHANGE_NAME, routing_key=''
        )

    @asyncio.coroutine
    def mq_connect(self):
        try:
            self._transport, self._protocol = yield from aioamqp.connect('localhost', 5672)
        except aioamqp.AmqpClosedConnection:
            print("closed connections")
            raise

        self._channel = yield from self._protocol.channel()
        yield from self._channel.exchange_declare(
            exchange_name=config.EXCHANGE_NAME, type_name='fanout'
        )


class Home(chilero.web.View):

    def get(self):
        payload = config.payload()
        yield from self.request.app.publish(payload)
        return chilero.web.JSONResponse(payload)


routes = [
    ['/', Home]
]

app = chilero.web.init(Application, routes)
