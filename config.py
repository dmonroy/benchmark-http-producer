import json
from datetime import datetime

import amqp

EXCHANGE_NAME = 'bench'


def payload():
    return {
        'event': 'pageview',
        'time': datetime.now().isoformat()
    }


class AMQPMixin:

    def connect(self):
        self._conn = amqp.Connection(
            host="localhost:5672",
            userid="guest",
            password="guest",
            virtual_host="/",
            insist=False
        )
        self._chan = self._conn.channel()

    def publish(self, payload):
        if not hasattr(self, '_chan'):
            self.connect()
        msg = amqp.Message(json.dumps(payload).encode('utf-8'))
        msg.properties["delivery_mode"] = 2

        self._chan.basic_publish(msg, exchange=EXCHANGE_NAME, routing_key='')