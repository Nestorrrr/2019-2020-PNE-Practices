from Seq0 import seq_read_fasta

FOLDER = "../Session_04/"
FILENAME = 'U5.txt'

DNA_FILE = FOLDER + FILENAME

seq_read_fasta(DNA_FILE)

print('DNA file: ', FILENAME)
print('The first 20 bases are: ', '\n', seq_read_fasta(DNA_FILE)[:20])