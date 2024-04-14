import cgitb
from http.server import HTTPServer, CGIHTTPRequestHandler

cgitb.enable()

server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()