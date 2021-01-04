#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except IndexError:
            x = 0
            print("out of range")
        except ZeroDivisionError:
            x = 0
            print("division by 0")
        except TypeError:
            x = 0
            print("wrong type")
        finally:
            result.append(x)
    return result
