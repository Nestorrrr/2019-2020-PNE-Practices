from Seq1 import Seq

print('-----| Practice 1, Exercise 10 |------')

FOLDER = "../Session_04/"
GENES = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
EXT = ".txt"
BASES = ['A', 'T', 'C', 'G']


for gene in GENES:
    sequence = Seq().read_fasta(FOLDER + gene + EXT)

    dictionary = sequence.count()

    lista = list(dictionary.values())

    maximo = max(lista)

    print(f"Gene {gene}: Most frequent Base: {BASES[lista.index(maximo)]}")