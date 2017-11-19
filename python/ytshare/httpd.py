#!/usr/bin/python3

import http.server
import socketserver
from ytshare_read import get_html

PORT = 4269

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(get_html().encode())


class MyTCPServer(socketserver.TCPServer):
    def __init__(self, host, ip):
        socketserver.TCPServer.__init__(self, host, ip)
        self.allow_reuse_address = True

with MyTCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
