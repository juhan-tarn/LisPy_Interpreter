#''hi --> 'HI
#(car ''hi) --> QUOTE
'''
Reference: https://github.com/norvig/pytudes/blob/master/py/lis.py
https://github.com/norvig/pytudes/blob/master/py/lis.py
https://github.com/norvig/pytudes/blob/master/py/lispy.py
'''
import re
import function_def
from function_def import dict_function

Symbol = str          # A Lisp Symbol is implemented as a Python str
List = list           #A Lisp list is implemented as a Python List
Num = int             # A Lisp number is implemented as integer


 ## evaluation on variables should just be error for now
 ## numbers evaluate to themselves
 ## for list, the first thing is always the funciton

def tokenize(chars):
    "convert chars to uppercase"

    "split a string into a list of tokens."
    return chars.replace('(', ' ( ').replace(')', ' ) ').replace('\'', ' \' ').split()

'''
use counting, if count is going to be negative, that's where
the closing parentheses gets added
'''
def convert_quote(tokens):  # ' +
    if '#' in tokens:
        sharp_index = int(tokens.index('#'))
        tokens[sharp_index] = '('
        tokens[sharp_index+1] = 'function'
        tokens.insert(sharp_index+3, ')')

        return tokens

    if '\'' not in tokens:
        return tokens
    quote_index = tokens.index('\'') #'a

    quote_list = tokens[(quote_index+1):]
    count = 0
    for i in range(quote_index+1, len(tokens)):
        if tokens[i] == '(':
            count += 1
        if tokens[i] == ')':
            count -= 1
        if count == 0:
            zero = i

    tokens.insert(zero+1, ')')
    tokens[quote_index] = '('
    tokens.insert(quote_index + 1, 'QUOTE')
    # while(quote_list):
    #     token = quote_list.pop(0)
    #     if token == '(':
    #         new_tokens.append(token)
    #         count += 1
    #     if token == ')':
    #         new_tokens.append(token)
    #         count += 1
    #
    #
    #
    #
    # new_tokens = []
    # count = 0
    # while(tokens):
    #     token = tokens.pop(0)
    #     if token == '\'':
    #         new_tokens.append('(')
    #         new_tokens.append('QUOTE')

    #
    # while(tokens):
    #     token = tokens.pop(0)
    #     if token == '\'':
    #         new_tokens.append('(')
    #         new_tokens.append('QUOTE')
    #         # print("tokens[0]: ", tokens[0])
    #         if tokens[0] != '(':
    #             new_tokens.append(tokens.pop(0))
    #             new_tokens.append(')')
    #         else:
    #             token = tokens.pop(0)
    #             while(token != ')'):
    #                 new_tokens.append(token)
    #                 token = tokens.pop(0)
    #             new_tokens.append(token)
    #             new_tokens.append(')')
    #     else:
    #         new_tokens.append(token)

    return convert_quote(tokens)


def read_from_tokens(tokens):
    "Read a list of tokens and build a tree (nested list) based on the expression."
    #if '#' not in tokens:
    tokens = convert_quote(tokens)

    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')
    token = tokens.pop(0)
    if '(' == token:
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens)) #recursively append lists to a big list --> build a tree
        tokens.pop(0) # pop off ')'
        return L
    elif ')' == token:
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

def atom(token):
    "Numbers become integers; every other token is a symbol."
    try:
        return int(token)
    except ValueError:
        return Symbol(token)

def parse(program):
    "Read a Scheme expression from a string."
    return read_from_tokens(tokenize(program))


def is_balanced(input):
    "Check if an expression has matching parentheses using basic arithmetics"
    sum = 0
    for i in range(len(input)):
        if sum < 0: #ensure that ) doesn't go first
            return False
        if input[i] == '(': # +1 when see (
            sum = sum + 1
        elif input[i] == ')': # -1 when see )
            sum = sum - 1
    if sum == 0:
        return True
    else:
        return False


def eval(parsed_input):
    try:
        return int(parsed_input) #when the input is a number, i.e. +3 or -3
    except: #when the input is a list
        '''
        if a list, do list thing
        if a string, do symbol thing
        '''
        if not parsed_input:
            return 'NIL'

        if not (isinstance(parsed_input, list)):
            if parsed_input.upper() == 'NIL':
                return "NIL"

        if parsed_input[0] == 'quote' or parsed_input[0] == 'QUOTE':
            # for i in parsed_input:
            #     if i.isalpha(): #convert to upper case if i is letters
            #         i = i.upper()
            return parsed_input[1] #[1] or [1:]?

        if parsed_input == 't' or parsed_input == 'T':
            return 'T'

        if parsed_input[0] == 'if':
            if(len(parsed_input[1:]))==3:
                if eval(parsed_input[1]) != 'NIL':
                    return eval(parsed_input[2])
                else:
                    return eval(parsed_input[3])
            elif len(parsed_input[1:]) == 2:
                if eval(parsed_input[1]) != 'NIL':
                    return eval(parsed_input[2])
                else:
                    return 'NIL'
        functions = dict_function #get the function dictionary
        if parsed_input[0] == 'function':
            return functions.get(parsed_input[1])
        if parsed_input[0] in functions:
            func = functions.get(parsed_input[0]) #get the operator and map to its function
            nested = parsed_input[1:] #save the rest of the list
            for i in range(len(nested)):
                #if(isinstance(nested[i], list)): # if the item is a list
                    element = eval(nested[i]) #recursively calculate the result of the nested list
                    nested[i] = element #replace the item with the result
                    #example: [ [- 1 3] [* 2 2]] --> [ -2 4]
            return func(nested)

def main():
    while True:
        try:
            userInput = input('lispy >') #raw_input return the input as string
        except EOFError:
            break
        if userInput == "Quit":
            break
        if not userInput:
            continue
        if is_balanced(userInput) == False:
            print("unmatching pairs of parentheses, try again")
            continue
        elif is_balanced(userInput) == True:
            print(eval(parse(userInput))) #create a print function for quote

if __name__ == '__main__':
    main()
