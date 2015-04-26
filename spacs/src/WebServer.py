import BaseHTTPServer
import LogHandler
import string
import os

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
            self.handle_api_call()
        else:
            LogHandler.log_warning("Web Request")
            self.handle_web_call()
    
    """
    Log that a request has been made. Occurs after headers are sent back.
    """
    def log_request(self, code=None, size=None):
        message = "Web Request: " + str(self.client_address[0]) + ":" + str(self.client_address[1])
        message += " " + self.command + " " + self.path + " (" + self.request_version + ")"
        message += " " + str(code)
        LogHandler.log_warning(message)
    
    """
    Handles all calls to the API
    """
    def handle_api_call(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>API</title></head>")
        self.wfile.write("<body>")
        self.wfile.write("%s" % self.path)
        self.wfile.write("</body>")
    
    """
    Handles all calls to the main web server
    """
    def handle_web_call(self):
        filetoserve = string.lower("www" + self.path)
        # Check for missing index.html
        if filetoserve[-1] == "/":
            filetoserve = filetoserve + "index.html"
        
        # Check the file exists
        if os.path.isfile(filetoserve):
            self.send_response(200)
        else:
            filetoserve = "WWW/errors/404.html"
            self.send_response(404)
        
        # Send Mime Type
        if filetoserve.endswith(".html"):
            self.send_header("Content-type", "text/html")
        elif filetoserve.endswith(".js"):
            self.send_header("Content-type", "application/javascript")
        elif filetoserve.endswith(".css"):
            self.send_header("Content-type", "text/css")
        else:
            self.send_header("Content-type", "application/octet-stream")
        self.end_headers()
        
        # Forward them the file
        f = open(filetoserve, 'r')
        for line in f:
            self.wfile.write(line)

