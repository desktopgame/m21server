from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from music21 import chord
from music21server.engine import Engine
import os
import sys
import json

# 対象のポート番号
port: int = 8080
if len(sys.argv) >= 1:
    try:
        port = int(sys.argv[-1])
    except:
        pass

address = ('localhost', port)
_server = None
_engine = Engine()


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global _server
        global _engine
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        if 'json' not in params:
            self.send_response(400)
            return
        query = params['json']
        if len(query) == 0:
            self.send_response(400)
            return
        print(f'- {query}')
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()
        try:
            obj = json.loads(query[0])
            self.wfile.write(json.dumps(
                {'status': 0, 'value': _engine.execute(obj)}).encode('utf-8'))
        except:
            print(f'!! {sys.exc_info()}')
            self.wfile.write(json.dumps(
                {'status': 1, 'value': {}}).encode('utf-8'))

    def do_POST(self):
        self.send_response(400)


def main():
    global _server
    global _engine
    with HTTPServer(address, MyHTTPRequestHandler) as server:
        _server = server
        while _engine.is_active:
            server.handle_request()
        server.server_close()


if __name__ == '__main__':
    main()
