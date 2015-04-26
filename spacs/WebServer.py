import BaseHTTPServer
import LogHandler

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

class WebServer(BaseHTTPServer.BaseHTTPRequestHandler):

    """
    Send HEAD response to client if that is all they have requested
    """
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    
    """
    Handle get requests to the server
    """
    def do_GET(s):
        LogHandler.log_warning("Received Request")
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Title goes here.</title></head>")
        s.wfile.write("<body>"+s)
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        s.wfile.write("</body></html>")
    