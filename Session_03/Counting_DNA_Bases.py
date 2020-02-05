def counter():
    print('Total lenght: ',len('CATGTAGACTAG'))
    i = 0
    counter_A = 0
    counter_C = 0
    counter_G = 0
    counter_T = 0
    while i < len('CATGTAGACTAG'):
        for e in 'CATGTAGACTAG':
            if e == 'A':
                counter_A += 1
                i += 1
            elif e == 'C':
                counter_C += 1
                i += 1
            elif e == 'G':
                counter_G += 1
                i += 1
            elif e == 'T':
                counter_T += 1
                i += 1
            else:
                print('The sequence has incorrect arguments')
    print('A: ', counter_A)
    print('C: ', counter_C)
    print('G: ', counter_G)
    print('T: ', counter_T)


counter()