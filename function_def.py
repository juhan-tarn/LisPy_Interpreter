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
    '''
    return the first element of the list
    '''
    flat_list = [item for sublist in input for item in sublist]
    return flat_list[0]

def cdr(input):
    '''
    return the list without the first element
    '''
    flat_list = [item for sublist in input for item in sublist]
    return flat_list[1:]

def listp(input):
    if(isinstance(input, list)):
        if str(input[0]).isdigit():
            return 'NIL'
        return 'T'
    return 'NIL'

def cons(input):
    result_list = []
    if len(input) > 2:
        print("too many arguments")
    elif input[0] == 'nil' or input[0] == 'NIL':
        result_list = list(input[1])
    elif input[1] == 'nil' or input[1] == 'NIL':
        result_list = list(input[0])
    else:
        result_list = input[1]
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


def _if(input): #move out from the function dictionary
    if len(input) == 3:
        if input[0] != 'NIL' :
            return input[1]
        else:
            return input[2]
    elif len(input)== 2:
        if input[0] == 'T':
            return input[1]
        else:
            return 'NIL'

def _and(input):
    for i in input:
        if i == 'NIL':
            return 'NIL'
    return input[-1]

def _or(input):
    for i in input:
        if i == 'NIL' or i == 'nil':
            continue
        else:
            return i
    return 'NIL'

def is_equal(input):
    ''' = for 2 arguments at most'''
    if(input < 2):
        print("not enough arguments")
    else:
        if input[0] == input[1]:
            return 'T'
    return 'NIL'

def is_Equal(input):
    return is_equal(input)

def progn(input):
    return input[-1]

#what to add to the func dictionary? name : op? should args be included?
def defun(input):
    operation = progn(input) #this is wrong
    name = input[0]
    if name not in dict_function:
        dict_function[name] = operation
    return name.upper()

def print_space():
    return ' '

def terpri():
    return '\n'

#['let', [['x', 1], ['y', 2]], ['+', 'x', 'y']]
#Q: when to pop it? how to know when to pop, what should let return?
def let(input):
    pop_list = []
    for i in input[0]:
        local_var = [i[0], i[1]]
        local_stack.append(local_var)
    for i in range(len(input[1:])):
        for j in range(len(local_stack)):
            if input[1:][i] == local_stack[j][0]:
                input[1:][i] = local_stack[j][1]
            pop_list.append(j)
    for i in pop_list:
        local_stack.pop(i)
    return input[1:]

def evaluation(input):
    if input[0] in dict_function:
        func = dict_function.get(input[0])
        nested = input[1:]
        for i in range(len(nested)):
            element = evaluation(nested[i])
            nested[i] = element
        return func(nested)

def apply(input):
    print(input)
    return input[0](input[-1])

def princ():
    return

def do(input):
    return

def load(input):
    return

def _lambda(input):
    return

def setq(input):
    key = input[0]
    value = input[1]
    global_dict[key] = value
    return value

def eval(input):
    return


#dictionary inspiration from: https://stackoverflow.com/questions/9168340/using-a-dictionary-to-select-function-to-execute
dict_function = {'+': add, '-': subtract, '*': multiply,
'/': divide, '<': is_less, '>': is_more, '<=':is_lessEqual,
'>=': is_moreEqual, 'list': list_, 'car': car, 'cdr': cdr,
'listp': listp, 'cons':cons, 'null':null, 'not': Not,
'and': _and, 'or': _or, 'progn': progn, '=': is_equal,
'equal':is_Equal, 'eval':eval, 'print-space':print_space,
'terpri':terpri, 'let':let, 'apply':apply, 'setq':setq}

local_stack = []
global_dict = {}



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
