
from Client0 import Client
from Seq1 import Seq

print(f"-----| Practice 2, Exercise 6 |------")

IP = "127.0.0.1"
PORT = 8080

FOLDER = "../Session_04/"
GENE = "FRAT1"
EXT = ".txt"

c = Client(IP, PORT)

print(c)

s = Seq().read_fasta(FOLDER + GENE + EXT)

bases = str(s)

print(f"Gene {GENE}: {bases}")

n = 10
c.talk(f"Sending {GENE} Gene to the server, in fragments of {n} bases...")

for i in range (5):
    frag = bases[i*n:(i+1)*n]
    c.talk(f"Fragment {i+1}: {frag}")
