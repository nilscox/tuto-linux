#!/usr/bin/python3

import http.server
import socketserver
from ytshare_read import get_html

PORT = 4269

class Handler(http.server.SimpleHTTPRequestHandler):
    def handle_request(self, func, *args, **kwargs):
        status = None
        content = None
        content_type = None

        try:
            status = 200
            content_type = 'text/html'
            content = func(*args, **kwargs)
        except e:
            status = 500
            content_type = 'text/plain'
            content = e.msg()

        content = content.encode()

        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.send_header('Content-length', len(content))
        self.end_headers()

        self.wfile.write(content)

    def do_GET(self):
        return self.handle_request(get_html)

class MyTCPServer(socketserver.TCPServer):
    def __init__(self, host, ip):
        socketserver.TCPServer.__init__(self, host, ip)
        self.allow_reuse_address = True

with MyTCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
