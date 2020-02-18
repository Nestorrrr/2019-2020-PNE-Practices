def fibonacci(user_input):
    my_list = []
    n = 0
    i = 1
    variable = 0
    variable_2 = 1
    while i < user_input+2:
        if i == 1:
            #print(n, end=' ')
            i += 1
            my_list.append(n)
        elif i == 2:
            #print(n + 1, end=' ')
            i += 1
            n += 1
            my_list.append(n)
        else:
            n = my_list[variable] + my_list[variable_2]
            variable += 1
            variable_2 += 1
            i += 1
            my_list.append(n)
            if i == user_input +2:
                print(user_input,'th Fibonacci term: ',n)


can_continue = False
while not can_continue:
    finish = False
    times = 0
    while not finish:
        user_input = int(input('Type here any integer number: '))
        fibonacci(user_input)
#       if user_input.isdigit():
#           fibonacci(user_input)
        times += 1
        if times == 3:
            finish = True
            can_continue = True
#       else:
#        print('You have to insert an integer number')
