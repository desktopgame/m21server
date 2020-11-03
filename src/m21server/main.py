from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from music21 import chord
import os
import sys
import json

# 対象のポート番号
port: int = 8080
if len(sys.argv) >= 1:
    try:
        port = int(sys.argv[1])
    except:
        pass

address = ('localhost', port)
vartable = {}
do_exit = False
_server = None


def callback(value):
    """
    引数のオブジェクトからmusic21を実行して結果を辞書で返します
    """
    global do_exit
    global vartable
    ret: dict = {}
    if 'command' not in value:
        return ret
    # コマンドごとに処理を分岐する
    command = value['command']
    if command == 'eval':
        expr = eval(value['source'])
        vartable[value['to']] = expr
        print(f'>> {expr}')
        ret = expr
    elif command == 'exit':
        do_exit = True
    else:
        raise f'unexpected command: {command}'
    return ret


class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global do_exit
        global _server
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
                {'status': 0, 'value': callback(obj)}).encode('utf-8'))
        except:
            print(f'!! {sys.exc_info()}')
            self.wfile.write(json.dumps(
                {'status': 1, 'value': {}}).encode('utf-8'))
        if do_exit:
            _server.server_close()

    def do_POST(self):
        self.send_response(400)


def main():
    global do_exit
    global _server
    with HTTPServer(address, MyHTTPRequestHandler) as server:
        _server = server
        while not do_exit:
            server.handle_request()


if __name__ == '__main__':
    main()
