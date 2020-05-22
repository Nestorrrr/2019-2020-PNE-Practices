from Client0 import Client
from Seq1 import Seq

print(f"-----| Practice 2, Exercise 5 |------")

IP = "127.0.0.1"
PORT = 8080

c = Client(IP, PORT)

FOLDER = "../Session_04/"
GENE = "U5"
EXT = ".txt"
file_name = FOLDER + GENE + EXT
sequence = Seq("")
sequence = str(sequence.read_fasta(file_name))


c.debug_talk(f"Sending the {GENE} Gene to the server...")
c.debug_talk(sequence)