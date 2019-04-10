def add(int_list):
    '''returns the sum of a given integer list'''
    result = int(sum(int_list))
    return result

def subtract(int_list):
    '''returns the difference between the first number and the rest of the list'''
    '''example: [- 10 1 2 3] is 10 - 1 - 2 - 3 = 4'''
    result = int_list[0]
    for x in int_list[1:]:
        result = result - x
    return result

def multiply(int_list):
    '''returns the product of the given list'''
    '''example: [* 1 2 3] is 1 * 2 * 3 = 6'''
    result = 1
    for x in int_list:
        result = result * x
    return result

def divide(int_list):
    '''divides two integers'''
    if len(int_list) == 2:
        return int(int_list[0]/int_list[1])
    elif int_list[1] == 0:
        print("Error: Division by zero.")
    else:
        print("too many or not enough arguments")

def is_less(int_list):
    '''<'''
    if len(int_list) == 2:
        if(int_list[0] < int_list[1]):
            return 'T'
        else:
            return 'NIL'
    else:
        print("too many or not enough arguments")

def is_more(int_list):
    '''>'''
    if len(int_list) == 2:
        if(int_list[0] > int_list[1]):
            return 'T'
        else:
            return 'NIL'
    else:
        print("too many or not enough arguments")

def is_lessEqual(int_list):
    '''<='''
    if len(int_list) == 2:
        if(int_list[0] <= int_list[1]):
            return 'T'
        else:
            return 'T'
    else:
        print("too many or not enough argument")

def is_moreEqual(int_list):
    ''' >= '''
    if len(int_list) == 2:
        if(int_list[0] >= int_list[1]):
            return True
        else:
            return False
    else:
        print("too many or not enough argument")

def list_(input):
    return list(input)

def car(input):
    flat_list = [item for sublist in input for item in sublist]
    return flat_list[0]

def cdr(input):
    flat_list = [item for sublist in input for item in sublist]
    return flat_list[1:]

def listp(input): #something is wrong
    if(isinstance(input, list)):
        return 'T'
    return 'NIL'

def cons(input):
    if len(input) > 2:
        print("too many arguments")
    elif input[0] == 'nil' or input[0] == 'NIL':
        result_list = list(input[1])
    elif input[1] == 'nil' or input[1] == 'NIL':
        result_list = list(input[0])
    else:
        result_list = input[1]
        #result_list = list(input[0]) + input[1]
        result_list.insert(0, input[0])
    return result_list

def null(input):
    if input[0] == 'nil' or input[0] == 'NIL' or input[0]==[]:
        return 'T'
    return 'NIL'

def Not(input):
    if null(input)=='T':
        print(null(input))
        return 'T'
    return 'NIL'

def quote_list(parsed_input):
    output = parsed_input[0]
    for i in range(1, len(parsed_input)):
        if(isinstance(parsed_input[i], list)):
            sub_string = quote_list(parsed_input[i])
            output = output + " " + sub_string
        else:
            output = output + " " + str(parsed_input[i])
    return "(" + output + ")"

def print_quotelist(parsed_input):
    temp = str(quote_list(parsed_input))
    temp = temp[:-1].split()
    final = " ".join(temp[1:])
    return final


'''
TODO:
EQUAL EVAL APPLY QUOTE FUNCTION IF AND OR NOT DEFUN
LIST CONS CAR CDR LISTP NULL NIL T
PROGN LET SETQ DO
PRINC TERPRI LOAD QUIT
'''

'''notes
(cons 'a 'b) --> Error
(cons 'a '(b)) --> (A B)
(cons '(a) '(b)) --> ((A) B)

'''

#dictionary inspiration from: https://stackoverflow.com/questions/9168340/using-a-dictionary-to-select-function-to-execute
def dic_function():
    dict = {'+': add, '-': subtract, '*': multiply, '/': divide, '<': is_less, '>': is_more, '<=':is_lessEqual, '>=': is_moreEqual, 'list': list_, 'car': car, 'cdr': cdr, 'listp': listp, 'cons':cons, 'null':null, 'not': Not}
    return dict
