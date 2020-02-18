from pathlib import Path

FILENAME = "RNU6_269P.txt"

file_contents = Path(FILENAME).read_text().split("\n")[1:] #separa desde la primera linea

final_contents = "\n".join(file_contents) #

print(final_contents)