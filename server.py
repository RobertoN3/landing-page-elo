"""Serve the landing page locally. Run: python server.py"""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        path = self.path.split('?')[0]
        if path not in ('/', '/index.html', '/elo-ring.png', '/favicon.ico'):
            self.send_error(404)
            return
        super().do_GET()

    def do_POST(self):
        self.send_error(404)

if __name__ == '__main__':
    print('elo: http://127.0.0.1:5174', flush=True)
    ThreadingHTTPServer(('127.0.0.1', 5174), Handler).serve_forever()
