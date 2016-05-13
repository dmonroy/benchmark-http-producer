import json

import config
import cherrypy


class HelloWorld(config.AMQPMixin, object):
    @cherrypy.expose
    def index(self):
        payload = config.payload()
        self.publish(payload)
        return json.dumps(payload)

app = cherrypy.tree.mount(HelloWorld())

