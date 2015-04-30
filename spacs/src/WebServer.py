import BaseHTTPServer
import LogHandler
import string
import os
import API
import json

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
            self.handle_api_call()
        else:
            self.handle_web_call()
    
    """
    Handle POST requests to the server
    """
    def do_POST(self):
        if string.lower(self.path).startswith("/api/"):
            self.handle_api_call()
        else:
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
        # Map API Calls to functions
        api_mapping={
                "default": API.bad_call,
                "invalid_data": API.invalid_data,
                "not_authed": API.not_authed,
                "auth/login": API.auth_login,
                "auth/logout": API.auth_logout,
                "ptu/update": API.not_implimented,
                "ptu/urgent": API.not_implimented,
                "psa/add": API.not_implimented,
                "psa/edit": API.not_implimented,
                "psa/remove": API.not_implimented,
                "po/add": API.not_implimented,
                "po/edit": API.not_implimented,
                "po/remove": API.not_implimented,
                "ptu/add": API.not_implimented,
                "ptu/edit": API.not_implimented,
                "ptu/remove": API.not_implimented
        }
        
        # Get the API Call and the parameter
        call = string.lower(self.path)[5:]
        parameter = ""
        if call.count('/') == 2:
            call, parameter = call.rsplit("/", 1)
        
        # Grab the data
        data_length = self.headers.getheader('content-length')
        if data_length == None:
            data = "{}"
        else:
            data_length = int(data_length)
            data = self.rfile.read(data_length)
        
        # Check data is valid JSON
        try:
            jsondata = json.loads(data)
        except ValueError, e:
            jsondata = json.loads("{}")
            call = "invalid_data"
        
        # Auth
        authed = False
        ret = ""
        try:
            ret = API.auth_login(jsondata, "")
        except KeyError:
            LogHandler.log_error("User failed to auth\r\n" + str(jsondata))
        if ret == {"error": "success"}:
            authed = True
        
        if not call.startswith("auth") and not authed:
            call = "not_authed"
        
        # Get the mapping
        try:
            command = api_mapping[call]
            self.send_response(200)
        except KeyError:
            LogHandler.log_warning("Illegal API Call: " + str(call))
            command = api_mapping["default"]
            self.send_response(400)
        
        # Finish Headers
        self.send_header("Content-type", "application/json")
        self.end_headers()
        
        # Execute the mapping and respond
        try:
            response = command(jsondata, parameter)
        except KeyError:
            LogHandler.log_error("data was malformed or missing\r\n" + str(jsondata))
            response = {"error": "failure"}
        if response == None:
            response = {}
        self.wfile.write(json.dumps(response))
    
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

