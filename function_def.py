
def add(int_list):
    result = int(sum(int_list))
    return result

def subtract(int_list):
    result = int_list[0]
    for x in int_list[1:]:
        result = result - x
    return result

def multiply(int_list):
    result = 1
    for x in int_list:
        result = result * x
    return result

def divide(int_list):
    if len(int_list) == 2:
        return int(int_list[0]/int_list[1])
    else:
        print("too many or not enough arguments")

def is_less(int_list):
    if len(int_list) == 2:
        if(int_list[0] < int_list[1]):
            return True
        else:
            return False
    else:
        print("too many or not enough arguments")

def is_more(int_list):
    if len(int_list) == 2:
        if(int_list[0] > int_list[1]):
            return True
        else:
            return False
    else:
        print("too many or not enough arguments")

def is_lessEqual(int_list):
    if len(int_list) == 2:
        if(int_list[0] <= int_list[1]):
            return True
        else:
            return False
    else:
        print("too many or not enough argument")

def is_moreEqual(int_list):
    if len(int_list) == 2:
        if(int_list[0] >= int_list[1]):
            return True
        else:
            return False
    else:
        print("too many or not enough argument")

'''
TODO:
EQUAL EVAL APPLY QUOTE FUNCTION IF AND OR NOT DEFUN
LIST CONS CAR CDR LISTP NULL NIL T
PROGN LET SETQ DO
PRINC TERPRI LOAD QUIT
'''

#dictionary inspiration from: https://stackoverflow.com/questions/9168340/using-a-dictionary-to-select-function-to-execute
def dic_function():
    dict = {'+': add, '-': subtract, '*': multiply, '/': divide, '<': is_less, '>': is_more, '<=':is_lessEqual, '>=': is_moreEqual}
    return dict
