# Function for calculating the sum of the N-first integer numbers


def sumn(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res


# -- The main program starts here
print("Sum of the 5 first integers: ", sumn(5))
print("Sum of the 10 first integers: ", sumn(10))
