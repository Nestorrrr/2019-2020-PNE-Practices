import pathlib
import http.server
import socketserver
import termcolor

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


def read_file(filename):
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    body = "".join(file_contents)
    return body

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        # Message to send back to the client
        FOLDER = "../P5/"
        if self.path == '/' or self.path =='/index.html':
            file = "index.html"

        else:
            file = self.path

        try:
            contents = read_file(FOLDER + file)
            self.send_response(200)
        except
