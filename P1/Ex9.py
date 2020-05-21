from Seq1 import Seq

print('-----| Practice 1, Exercise 9 |------')

FOLDER = "../Session_04/"
file_name = FOLDER + "U5.txt"

sequence = Seq("")
sequence = sequence.read_fasta(file_name)

print(f"Sequence :  (Lenght: {sequence.len()})  {sequence}")
print(f"Bases: {sequence.count()}")
print(f"Rev: {sequence.reverse()}")
print(f"Comp: {sequence.complement()}")