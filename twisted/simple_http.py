# How to start it:
#   on windows: twistd.py --python simple_http.py
#   on linux:   twistd --python simple_http.py
from twisted.web import http
from twisted.python import log
from twisted.application import internet, service


class MyRequestHandler(http.Request):
    pages = {
        '/': '<h1>Home</h1>Home Page',
        '/test': '<h1>Test</h1>Test Page',
    }

    def process(self):
        log.msg("Client " + self.getClientIP() + " request " + str(self.args))
        if self.path in self.pages:
            self.write(self.pages[self.path])
        else:
            self.setResponseCode(http.NOT_FOUND)
            self.write("<h1>Not Found</h1>Sorry, no such page.")
        self.finish()


class MyHttp(http.HTTPChannel):
    requestFactory = MyRequestHandler


class MyHttpFactory(http.HTTPFactory):
    protocol = MyHttp


# configuration parameters
port = 10000
listen_ip = 'localhost'

# this will hold the services that combine to form the poetry server
top_service = service.MultiService()

# the tcp service connects the factory to a listening socket. it will
# create the listening socket when it is started
factory = MyHttpFactory()
tcp_service = internet.TCPServer(port, factory, interface=listen_ip)
tcp_service.setServiceParent(top_service)

# this variable has to be named 'application'
application = service.Application("simple_http")

# this hooks the collection we made to the application
top_service.setServiceParent(application)
