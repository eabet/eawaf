import os
from google.appengine.ext.webapp import template

import logging

class tmpl():
    def __init__( self, instance, filename ):
        self.filename        = filename
        self.response        = instance.response
        self.values          = {}
        self.path            = 'templates/' + self.filename

    # def test( self, **values ):
    #     logging.getLogger().setLevel(logging.DEBUG)
    #     logging.debug(values)

    def set( self, **values ):
        for k,v in values.items():
            self.values[k] = v

    def render(self):
        self.path = os.path.join(os.path.dirname(__file__), self.path)
        self.response.out.write(
            template.render(self.path, self.values)
        )
