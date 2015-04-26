import BaseHTTPServer
import LogHandler
import string

def start():
    PORT = 8000
    HOSTNAME = ""
    httpd = BaseHTTPServer.HTTPServer((HOSTNAME, PORT), WebServer)
    print "serving at port", PORT
    while True:
        try:
            httpd.serve_forever()
        except:
            LogHandler.log_exception()

def health():
    pass


"""
This class handles all the requests that the web server recieves
"""
class WebServer(BaseHTTPServer.BaseHTTPRequestHandler):

    """
    Send HEAD response to client if that is all they have requested
    """
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    
    """
    Handle GET requests to the server
    """
    def do_GET(self):
        if string.lower(self.path).startswith("/api/"):
            LogHandler.log_warning("API Request")
        else:
            LogHandler.log_warning("Web Request")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        #self.wfile.write("<html><head><title>Title goes here.</title></head>")
        self.wfile.write("<body>")
        self.wfile.write("<p>You accessed path: %s</p>" % self.path)
        self.wfile.write("</body>")
    
    """
    Log that a request has been made. Occurs after headers are sent back.
    """
    def log_request(self, code=None, size=None):
        message = "Web Request: " + str(self.client_address[0]) + ":" + str(self.client_address[1])
        message += " " + self.command + " " + self.path + " (" + self.request_version + ")"
        message += " " + str(code)
        LogHandler.log_warning(message)
    