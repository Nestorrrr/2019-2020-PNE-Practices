import http.server
import socketserver
import termcolor
from pathlib import Path

PORT = 8080

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_Get(self):
        termcolor.cprint(self.requestline, 'blue')

        body = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>FORM !</title>
        </head>
        <body>
            <form action = 'echo' method = 'get'>
                Message to send to the server: <br>
                < input type = 'text' name = 'msg'>
                <input type = 'submit' value = 'SEND'>
            </form>
        </body>
        </html>
        """

        if self.path == '/':
            file = 'form-1.html'