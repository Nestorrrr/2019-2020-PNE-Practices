import pathlib
import http.server
import socketserver
import termcolor

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True


def read_file(filename):
    file_contents = pathlib.Path(filename).read_text().split('\n')[1:]
    body = "".join(file_contents)
    return body


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'green')

        FOLDER = "../P5/"
        EXT = '.html'
        print(self.path)

        if self.path == '/' or self.path == '/index.html':
            file = 'index.html'

        else:
            file = self.path
            file += '.html'

        try:
            contents = read_file(FOLDER + file )
            self.send_response(200)

        except FileNotFoundError:
            contents = read_file(FOLDER + 'Error.html')
            self.send_response(404)

        self.send_header('Content/Type: ', 'text/html')
        self.send_header('Content/Length: ', len(contents.encode()))

        self.end_headers()
        self.wfile.write(contents.encode())  # Send the response message

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()
