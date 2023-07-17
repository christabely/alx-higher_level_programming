#!/usr/bin/python3
def no_c(my_string):
    length = len(my_string)

    k = 0

    new_string = my_string[:]

    for k in range(length):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            new_string = new_string[:(i - k)] + my_string[(i + 1):]
            k += 1

    return (new_string)
