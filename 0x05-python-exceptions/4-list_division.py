#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_List = []
    for i in range(list_length):
        try:
            d = (my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            d = 0
            print("division by 0")
        except TypeError:
            d = 0
            print("wrong type")
        except IndexError:
            d = 0
            print("out of range")
        finally:
            new_List.append(d)
    return new_List
