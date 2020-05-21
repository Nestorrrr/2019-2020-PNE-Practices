from Seq1 import Seq

print('-----| Practice 1, Exercise 6 |------')

sequence1 = Seq()
sequence2 = Seq("ACTGA")
sequence3 = Seq("Invalid sequence")

print(f"Sequence 1:  (Lenght: {sequence1.len()})  {sequence1}")
print(f"Bases: {sequence1.count()}")
print(f"Rev: {sequence1.reverse()}")

print(f"Sequence 2:  (Lenght: {sequence2.len()})  {sequence2}")
print(f"Bases: {sequence2.count()}")
print(f"Rev: {sequence2.reverse()}")

print(f"Sequence 3:  (Lenght: {sequence3.len()})  {sequence3}")
print(f"Bases: {sequence3.count()}")
print(f"Rev: {sequence3.reverse()}")
