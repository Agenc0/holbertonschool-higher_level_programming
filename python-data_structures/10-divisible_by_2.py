#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    statuslist = [i % 2 == 0 for i in my_list]
    return statuslist
