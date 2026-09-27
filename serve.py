# Serves ONLY the 3D house page (index.html) from the project folder on 127.0.0.1:8765,
# so the tunnel exposes the model and nothing else in the folder (e.g. the map photo).
import functools
import http.server

ROOT = r'S:\testing\3d\3d threejs home'


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path.split('?')[0] not in ('/', '/index.html'):
            self.send_error(404)
            return
        super().do_GET()

    def do_HEAD(self):
        self.do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')        # edits to index.html show up on refresh
        super().end_headers()


http.server.ThreadingHTTPServer(('127.0.0.1', 8765), functools.partial(Handler, directory=ROOT)).serve_forever()
