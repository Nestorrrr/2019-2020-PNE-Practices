class Seq:

    def __init__(self, strbases):
        bases = ['A', 'C', 'G', 'T']
        for element in strbases:
            if element not in bases:
                print('ERROR!!')
                self.strbases = 'ERROR'
                return
        self.strbases = strbases
        print('New sequence created')

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


def print_seqs(seqs):
    for seq in seqs:
        print(f'Sequence {seqs.index(seq)}: (Length: {seq.len()})  {seq}')


def generate_seqs(pattern, number):
    new_seq = []

    for i in range(1, number + 1):
        new_seq.append(Seq(pattern * i))
    return new_seq