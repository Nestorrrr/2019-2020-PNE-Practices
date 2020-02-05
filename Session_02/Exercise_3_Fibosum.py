def sumfibonacci():
    lista = []
    total = 0
    n = 0
    i = 1
    variable = 0
    variable_2 = 1
    while i <= 6:
        if i == 1:
            i += 1
            lista.append(n)
            total += n
        elif i == 2:
            i += 1
            n += 1
            lista.append(n)
            total += n
        else:
            n = lista[variable] + lista[variable_2]
            variable += 1
            variable_2 += 1
            i += 1
            lista.append(n)
            total += n
    print('Sum of the First 5 terms of the Fibonacci series: ', total)


def sumfibonacci_2():
    lista = []
    total = 0
    n = 0
    i = 1
    variable = 0
    variable_2 = 1
    while i <= 11:
        if i == 1:
            i += 1
            lista.append(n)
            total += n
        elif i == 2:
            i += 1
            n += 1
            lista.append(n)
            total += n
        else:
            n = lista[variable] + lista[variable_2]
            variable += 1
            variable_2 += 1
            i += 1
            lista.append(n)
            total += n
    print('Sum of the First 5 terms of the Fibonacci series: ', total)


sumfibonacci()
sumfibonacci_2()
