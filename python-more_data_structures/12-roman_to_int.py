#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

        def assigner(letter):
            ronumbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}
            if letter not in ronumbers:
                return -1
            else:
                return ronumbers[letter]

        res, i = 0
        while i < len(roman_string):
            inum = assigner(roman_string[i])

            if i + 1 < len(roman_string):
                next_num = assigner(roman_string[i + 1])
                if inum >= next_num:
                    res += inum
                    i += 1
                else:
                    res += next_num - inum
                    i += 2
            else:
                res += inum
                i += 1

        return res
