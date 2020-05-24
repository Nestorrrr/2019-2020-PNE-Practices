import http.server
import socketserver
import termcolor
import json
from pathlib import Path

PORT = 8080
IP = '127.0.0.1'
Bases = ['A', 'C', 'G', 'T']

database = 'rest.ensembl.org'
parameters = '?content-type=application/json'
conn = http.client.HTTPConnection(database)

socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        termcolor.cprint(self.requestline, 'blue')
        req_line = self.requestline.split(' ')
        arguments = (req_line[1]).split('?')

        first_argument = arguments[0]

        contents = Path('Error.html').read_text()
        self.send_response(404)

        try:

            if first_argument == '/':
                contents = Path('index.html').read_text()
                self.send_response(200)

            elif first_argument == '/listSpecies':
                contents = f"""<!DOCTYPE html> 
                                    <html lang = "en">
                                    <head>
                                     <meta charset = "utf-8" >
                                     <title>List of species in the browser</title >
                                    </head >
                                    <body  style="background-color:#FFF0F5">
                                     <h1 style="color:#CD5C5C;"> List of species in the genome database</h1>
                                     <p style="color:#CD5C5C;"><b>The total number of species in ensembl is: 286</b></p>"""

                get_value = arguments[1]
                seq_n = get_value.split('?')
                seq_name, index = seq_n[0].split('=')

                if index == '':
                    index = '286'
                elif index == str:
                    contents = """f<!DOCTYPE html>
                                                        <html lang="en">
                                                            <head>
                                                                <meta charset="UTF-8">
                                                                <title>Error</title>
                                                            </head>
                                                            <body style="background-color:#FFF0F5">
                                                                <h1>ERROR</h1>
                                                                <p style="color:#CD5C5C;"><b>Selected specie's karyotype information is not available</b></p>
                                                                <p style="color:#CD5C5C;"><b> Introduce a specie in the database to find its karyotype</b></p>
                                                                <a href="/"> Main page </a> </p>
                                                                </body>
                                                                </html>"""
                index = int(index)
                if index <= 0:
                    contents = f"""<!DOCTYPE html>
                                <html lang="en" dir="ltr">
                                  <head>
                                    <meta charset="utf-8">
                                    <title>ERROR</title>
                                  </head>
                                  <body style="background-color: red;">
                                    <h1>ERROR</h1>
                                    <p>Resource not available</p>
                                    <p>Your search's limit is equal or less than 0</p>
                                    <a href="/"> Main page </a> </p>
                                  </body>
                                </html>"""
                elif index > 0:
                    contents += f"""<p>The number of species you selected are: {index} </p>"""
                    endpoint = 'info/species'
                    parameters = '?content-type=application/json'
                    request = endpoint + parameters

                    try:
                        conn.request('GET', request)

                    except ConnectionRefusedError:
                        print('Error!!! Cannot connect to the Server')
                        exit()

                    response = conn.getresponse()
                    body = response.read().decode('utf-8')
                    limit_list = []
                    body = json.loads(body)
                    limit = body['species']

                    if index > len(limit):
                        contents = f"""!DOCTYPE html>
                                                    <html lang = "en">
                                                    <head>
                                                     <meta charset = "utf-8" >
                                                     <title>ERROR</title >
                                                    </head>
                                                    <body  style="background-color:#FFF0F5">
                                                    <p style="color:#CD5C5C;"><b>ERROR LIMIT OUT OF RANGE</b></p>
                                                    <p style="color:#CD5C5C;"><b>Introduce a valid limit</b></p>
                                                    <a href="/">Main page</a></body></html>"""
                    else:
                        for element in limit:
                            limit_list.append(element['display_name'])

                            if len(limit_list) == index:
                                contents += f"""<p>The species are: </p>"""
                                for specie in limit_list:
                                    contents += f"""<p> - {specie} </p>"""
                        contents += f"""<a href="/">Main page</a></body></html>"""


            elif first_argument == '/karyotype':
                contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                    <meta charset = "utf-8">
                                     <title> Karyotype </title >
                                </head >
                                <body  style="background-color:#DB7093">
                                """
                try:
                    get_value = arguments[1]
                    specie = get_value.split('?')
                    specie_method, sp_name = specie[0].split('=')

                    full_name = ''
                    for n in range(0, len(sp_name)):
                        if sp_name[n] == '+':
                            full_name += '%20'
                        else:
                            full_name += sp_name[n]

                    endpoint = 'info/assembly/'
                    parameters = '?content-type=application/json'
                    request = endpoint + full_name + parameters

                    try:
                        conn.request('GET', request)

                    except ConnectionRefusedError:
                        print('Error!!! Cannot connect to the Server')
                        exit()

                    response = conn.getresponse()
                    body = response.read().decode('utf-8')
                    body = json.loads(body)
                    karyotype_info = body['karyotype']

                    full_name = full_name.replace('%20',' ')
                    contents += f"""<h2 style="color:#DB7093;"> The names of the {full_name} chromosomes are:</h2>"""

                    for chromosome in karyotype_info:
                        contents += f"""<p> - {chromosome} </p>"""

                    contents += f"""<a href="/">Main page </a></body></html>"""

                except KeyError:
                    contents = f"""<!DOCTYPE html> 
                                    <html lang="en">
                                        <head>
                                            <meta charset="UTF-8">
                                            <title>Error</title>
                                        </head>
                                        <body style="background-color:PALETURQUOISE">
                                            <h1 style="color:#DB7093;">ERROR</h1>
                                            <p style="color:#DB7093;"> Selected specie's karyotype information is not available </p>
                                            <p><a href="/Karyotype?Specie={full_name}">Check if your specie is in our database</a><br><br>
                                            <p style="color:#DB7093;"> Introduce a specie in the database to find its karyotype </p>
                                            <a href="/"> Main page </a> </p>
                                            </body>
                                            </html>"""

                    #else:
         #   contents = Path('Error.html').read_text()

        self.send_response(200)
        self.send_header('Content/Type', 'text/html')
        self.send_header('Content/Length', len(contents.encode()))
        self.end_headers()
        self.wfile.write(contents.encode())

        return


Handler = TestHandler

with socketserver.TCPServer(('', PORT), Handler) as httpd:
    print('Server at PORT', PORT)
    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        print('')
        print('Stopped by the user')
        httpd.server_close()
