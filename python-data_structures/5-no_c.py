#!/usr/bin/python3
def no_c(my_string):
    noC = ""
    for i in my_string:
        if i != C and i != c:
            noC += i
    return noC
