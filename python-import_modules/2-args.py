#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv
    argnum = len(args) - 1

    print(f"{argnum}", end=" ")
    if argnum == 0:
        print("arguments.")
    elif argnum == 1:
        print("argument:")
    else:
        print ("arguments:")

    for i in range(argnum):
        print("{}: {}".format(i + 1, args[i + 1]))
