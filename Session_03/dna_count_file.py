DNA_list = []
with open('dna.txt', 'r') as f:
    for line in f:
        f = line.replace('\n', '')
    DNA_list.append(f)
print(DNA_list)