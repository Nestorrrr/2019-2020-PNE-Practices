from pathlib import Path


class Seq:

    NULL = "NULL"
    ERROR = "ERROR"

    def __init__(self, strbases=NULL):
        if strbases == self.NULL:
            self.strbases = self.NULL
            print("NULL Seq created")
            return

        if not self.valid_str(strbases):
            self.strbases = self.ERROR
            print("INVALID Seq!")
            return

        self.strbases = strbases
        print('New sequence created')

    def __str__(self):
        return self.strbases

    @staticmethod
    def valid_str(strbases):

        valid_bases = ['A', 'C', 'T', 'G']

        for element in strbases:
            if element not in valid_bases:
                return False

        return True

    def len(self):
        if self.strbases in [self.NULL, self.ERROR]:
            return 0
        else:
            return len(self.strbases)


def print_seqs(seqs):
    for seq in seqs:
        print(f'Sequence {seqs.index(seq)}: (Length: {seq.len()})  {seq}')


def generate_seqs(pattern, number):
    new_seq = []

    for i in range(1, number + 1):
        new_seq.append(Seq(pattern * i))
    return new_seq