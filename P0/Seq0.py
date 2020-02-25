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

def seq_count_base():
    file_contents = pathlib.Path(filename).read_text().split("\n")[1:]
    seq = "".join(file_contents)