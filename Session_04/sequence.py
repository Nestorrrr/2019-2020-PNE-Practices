from pathlib import Path

FILENAME = "U5.txt"

file_contents = Path(FILENAME).read_text().split("\n")[1:] # elimina primer elemento

seq = "".join(file_contents) #"" va como lo unes

print(seq)
