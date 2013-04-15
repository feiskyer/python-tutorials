"""
http://jcalderone.livejournal.com/49707.html
http://labs.twistedmatrix.com/2008/02/simple-python-web-server.html

usage:
        $ twistd -y webserver.py
"""


from pprint import pprint
from twisted.application import internet
from twisted.application.service import Application
from twisted.web.resource import Resource
from twisted.web.server import Site


class FormPage(Resource):
    def render_GET(self, request):
        return 'form'

    def render_POST(self, request):
        pprint(request.__dict__)
        newdata = request.content.getvalue()
        print newdata
        return ''

class HelloPage(Resource):
    def render_GET(self, request):
        return "hello"

root = Resource()
root.putChild("form", FormPage())
root.putChild("hello", HelloPage())
application = Application("My Web Service")
internet.TCPServer(10000, Site(root, timeout=60*15)).setServiceParent(application)