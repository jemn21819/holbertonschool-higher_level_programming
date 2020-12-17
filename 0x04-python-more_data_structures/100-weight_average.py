#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    var1 = 0
    var2 = 0
    for i, j in my_list:
        var1 += i * j
        var2 += j
    return (var1 / var2)
