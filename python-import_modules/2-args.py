#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argnum = sys.argv
    arglen = len(argnum) - 1

    if arglen > 1:
        print(arglen, "arguments:")
        for i in range(1, arglen + 1):
            print("{}: {}".format(i, argnum[i]))
    elif arglen == 1:
        print(arglen, "argument:")
        for i in range(1, arglen + 1):
            print("{}: {}".format(i, argnum[i]))
    else:
        print(arglen, "arguments.")
