import socket
import termcolor

# Configure the Server's IP and PORT
IP = "127.0.0.1"
PORT = 8080

SEQ_GET = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT",
]


def get_cmd(n):
    return SEQ_GET[n]


# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("Seq server is configured!")

# --- MAIN LOOP
while True:
    print('Waiting for clients...')
    try:
        (cs, client_ip_port) = ls.accept()

    except KeyboardInterrupt:
        print('Server Stopped!')
        ls.close()
        exit()

    else:

        req_raw = cs.recv(2000)
        req = req_raw.decode()

        lines = req.split("\n")
        line0 = lines[0].strip()

        lcmds = line0.split(' ')
        cmd = lcmds[0]

        try:
            arg = lcmds[1]

        except IndexError:
            arg = ''

        response = ''

        if cmd == 'PING':
            termcolor.cprint('PING Command!', 'green')
            response = 'OK!'

        elif cmd == 'GET':
            termcolor.cprint('GET', 'green')
            response = get_cmd(int(arg))

        response += '\n'
        print(response)
        cs.send(response.encode())
        cs.close()
