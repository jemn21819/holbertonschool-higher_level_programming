#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is str and roman_string:
        num = 0
        x = roman_string
        ro = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        for i in range(len(roman_string)):
            if i < len(x) - 1:
                num += ro[x[i]] if ro[x[i]] >= ro[x[i + 1]] else ro[x[i]] * -1
            else:
                num += ro[x[i]]
        return num
    else:
        return 0
