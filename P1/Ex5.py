from Seq1 import Seq

print('-----| Practice 1, Exercise 5 |------')

sequence1 = Seq()
sequence2 = Seq("ACTGA")
sequence3 = Seq("Invalid sequence")

print(f"Sequence 1:  (Lenght: {sequence1.len()})  {sequence1}")
print(f"A: {sequence1.count_base('A')} ,C: {sequence1.count_base('C')}, G: {sequence1.count_base('G')}, T: {sequence1.count_base('T')}")
print(f"Sequence 2:  (Lenght: {sequence2.len()})  {sequence2}")
print(f"A: {sequence2.count_base('A')} ,C: {sequence2.count_base('C')}, G: {sequence2.count_base('G')}, T: {sequence2.count_base('T')}")
print(f"Sequence 3:  (Lenght: {sequence3.len()})  {sequence3}")
print(f"A: {sequence3.count_base('A')} ,C: {sequence3.count_base('C')}, G: {sequence3.count_base('G')}, T: {sequence3.count_base('T')}")