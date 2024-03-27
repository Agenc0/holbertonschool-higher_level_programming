#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argnum = sys.argv
    arglen = len(argnum) - 1

    print("{}".format(arglen), end=" ")
    if arglen == 0:
        print("arguments.")
    elif arglen == 1:
        print("argument:")
    else:
        print("arguments:")

    for i in range(arglen):
        print("{}: {}".format(i + 1, argnum[i + 1]))
