import socket
import pathlib
import termcolor

IP = '127.0.0.1'
PORT = 8080


def read(filename):
    file_contents = pathlib.Path(filename).read_text().split('\n')[1:]
    body = "".join(file_contents)
    return body


def process_client(s):
    req_raw = s.recv(2000)
    req = req_raw.decode()

    print('Message FROM CLIENT: ')

    lines = req.split('\n')
    req_line = lines[0]

    print('Request line: ', end='')
    termcolor.cprint(req_line, 'green')

    FOLDER = '../P4/'

    if '/info/A' in req_line:
        FILENAME = 'A.html'
        body = read(FOLDER + FILENAME)
    elif '/info/C' in req_line:
        FILENAME = 'C.html'
        body = read(FOLDER + FILENAME)
    elif '/info/G' in req_line:
        FILENAME = 'G.html'
        body = read(FOLDER + FILENAME)
    elif '/info/T' in req_line:
        FILENAME = 'T.html'
        body = read(FOLDER + FILENAME)
    else:
        FILENAME = 'Error.html'
        body = read(FOLDER + FILENAME)

    status_line = 'HTTP/1.1 200 OK\n'
    header = 'Content-Type: text/html\n'
    header += f'Content-Length: {len(body)}\n'

    response_msg = status_line + header + '\n' + body
    cs.send(response_msg.encode())


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ls.bind((IP, PORT))
ls.listen()
print('SEQ Server configured!')

while True:
    print('Waiting for clients to connect...')
    try:
        (cs, client_ip_port) = ls.accept()
    except KeyboardInterrupt:
        print('Server stopped!')
        ls.close()
        exit()
    else:
        process_client(cs)
        cs.close()
