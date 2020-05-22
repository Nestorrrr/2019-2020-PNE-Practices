from Client0 import Client
from Seq1 import Seq

print(f"-----| Practice 2, Exercise 6 |------")

IP = "127.0.0.1"
PORT = 8080
PORT2 = 8081

c = Client(IP,PORT)
c2 = Client(IP,PORT2)

print(c)
print(c2)

FOLDER = "../Session_04/"
GENE = "FRAT1"
EXT = ".txt"

s = Seq().read_fasta(FOLDER + GENE + EXT)

bases = str(s)

print(f"Gene {GENE}: {bases}")

n = 10
c.talk(f"Sending {GENE} Gene to the server, in fragments of {n} bases...")
c2.talk(f"Sending {GENE} Gene to the server, in fragments of {n} bases...")

i=1
for i in range (10):
    frag = bases[i*n:(i+1)*n]
    if i % 2 == 0:
        print(f"Fragment {i + 1}: {frag}")
        c.talk(f"Fragment {i + 1}: {frag}")
    else:
        print(f"Fragment {i + 1}: {frag}")
        c2.talk(f"Fragment {i + 1}: {frag}")
