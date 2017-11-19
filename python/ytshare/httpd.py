#!/usr/bin/python3

import http.server
import socketserver
from ytshare_read import get_html
from ytshare import save_youtube_id

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
        except Exception as e:
            status = 500
            content_type = 'text/plain'
            content = str(e)

        content = content.encode()

        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.send_header('Content-length', len(content))
        self.end_headers()

        self.wfile.write(content)

    def do_GET(self):
        return self.handle_request(get_html)

    def do_POST(self):
        content_len = int(self.headers.get('content-length'))
        content = self.rfile.read(content_len)

        return self.handle_request(save_youtube_id, content.decode())


socketserver.TCPServer.allow_reuse_address = True

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
