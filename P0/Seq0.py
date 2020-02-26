import pathlib


def seq_ping():
    print('OK')


def seq_read_fasta(filename):
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]  # elimina primer elemento
    seq = "".join(file_contents)  # "" va como lo unes
    return seq


def seq_len(filename):
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    seq = "".join(file_contents)
    return len(seq)


def seq_count_base(filename):
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    seq = "".join(file_contents)
    print('A: ',seq.count('A'))
    print('C: ',seq.count('C'))
    print('G: ',seq.count('G'))
    print('T: ',seq.count('T'))


def seq_count(filename,user_input):
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    seq = "".join(file_contents)
    dictionary = {'A': seq.count('A'), 'C': seq.count('C'), 'G': seq.count('G'), 'T': seq.count('T')}
    print('Gene ', user_input, ': ',dictionary)


def seq_reverse(filename, user_input):
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    seq = "".join(file_contents)
    seq_final = seq[:20]
    print('Gene ', user_input, ':','\n','Frag: ', seq_final,'\n','Rev: ', seq_final[::-1])


def seq_complement(filename, user_input):
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    seq = "".join(file_contents)
    seq_final = seq[:20]
    print('Gene ',user_input, ':','\n','Frag: ',seq_final,'\n', 'Comp: ',end='')
    for element in seq_final:
        if element == 'A':
            print('T', end='')
        elif element == 'C':
            print('G', end='')
        elif element == 'G':
            print('C', end='')
        elif element == 'T':
            print('A', end='')
    print('\n')


def seq_count_frecuentest_base(filename,user_input):
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    seq = "".join(file_contents)
    lista = [seq.count('A'),seq.count('C'),seq.count('G'),seq.count('T')]
    number = max(lista)
    for element in lista:
        if number == seq.count('A'):
            solution = 'A'
        elif number == seq.count('C'):
            solution = 'C'
        elif number == seq.count('G'):
            solution = 'G'
        elif number == seq.count('T'):
            solution = 'T'
    print('Gene ',user_input,': Most frequent Base: ',solution)