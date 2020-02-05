def counting_file():
    try:
        with open('dna.txt', 'r') as f:
            print(f)
            for line in f:
                line.replace('\n', '')
            print(f)
    except Exception as e:
        print(e)
    f.close()


counting_file()
