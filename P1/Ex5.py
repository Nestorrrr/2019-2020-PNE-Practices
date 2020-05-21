from Seq1 import Seq

print('-----| Practice 1, Exercise 5 |------')

sequence1 = Seq()
sequence2 = Seq("ACTGA")
sequence3 = Seq("Invalid sequence")

print(f"Sequence 1:  (Lenght: {sequence1.len()})  {sequence1}  {sequence1.count_base}")
print(f"Sequence 2:  (Lenght: {sequence2.len()})  {sequence2}  {sequence2.count_base}")
print(f"Sequence 3:  (Lenght: {sequence3.len()})  {sequence3}  {sequence3.count_base}")