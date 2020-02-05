def fibonacci():
    lista = []
    n = 0
    i = 1
    variable = 0
    variable_2 = 1
    while i < 12:
        if i == 1:
            print(n,end=' ')
            i += 1
            lista.append(n)
        elif i == 2:
            print(n + 1, end=' ')
            i += 1
            n += 1
            lista.append(n)
        else:
            n = lista[variable] + lista[variable_2]
            variable += 1
            variable_2 += 1
            i += 1
            lista.append(n)
            print(n, end=' ')


fibonacci()
