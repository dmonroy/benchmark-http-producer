import json

import config

from flask import Flask


class MyApp(config.AMQPMixin, Flask):
    pass

app = MyApp(__name__)


@app.route('/')
def hello_world():

    payload = config.payload()

    app.publish(payload)

    return json.dumps(payload)

if __name__ == '__main__':
    app.run()
