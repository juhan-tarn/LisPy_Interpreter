#''hi --> 'HI
#(car ''hi) --> QUOTE
'''
Reference: https://github.com/norvig/pytudes/blob/master/py/lis.py
https://github.com/norvig/pytudes/blob/master/py/lis.py
https://github.com/norvig/pytudes/blob/master/py/lispy.py
'''
import re
import function_def

Symbol = str          # A Lisp Symbol is implemented as a Python str
List = list           #A Lisp list is implemented as a Python List
Num = int             # A Lisp number is implemented as integer

 ## evaluation on variables should just be error for now
 ## numbers evaluate to themselves
 ## for list, the first thing is always the funciton

def tokenize(chars):
    "convert chars to uppercase"
    # if 'QUOTE' in chars.upper():
    #    chars = chars.upper()
    "split a string into a list of tokens."
    return chars.replace('(', ' ( ').replace(')', ' ) ').replace('\'', ' \' ').split()


def convert_quote(tokens):
    if '\'' not in tokens:
        return tokens
    new_tokens = []
    while(tokens):
        token = tokens.pop(0)
        if token == '\'':
            new_tokens.append('(')
            new_tokens.append('QUOTE')
            # print("tokens[0]: ", tokens[0])
            if tokens[0] != '(':
                new_tokens.append(tokens.pop(0))
                new_tokens.append(')')
            else:
                token = tokens.pop(0)
                while(token != ')'):
                    # print("this token: ", token)
                    # print("condition value: ", (token != ')'))
                    # print("remain: ", tokens)
                    new_tokens.append(token)
                    token = tokens.pop(0)
                    #new_tokens.append(token)
                new_tokens.append(token)
                new_tokens.append(')')
        else:
            new_tokens.append(token)
    print(new_tokens)
    return new_tokens




def read_from_tokens(tokens):
    "Read a list of tokens and build a tree (nested list) based on the expression."
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
    print(parsed_input)
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

        if parsed_input[0] == 'QUOTE':
            # for i in parsed_input:
            #     if i.isalpha(): #convert to upper case if i is letters
            #         i = i.upper()
            return parsed_input[1]

        #if 'QUOTE' in parsed_input:
            #return parsed_input[1]
            #return quote_list(parsed_input)
            #return print_quotelist(parsed_input)
        functions = function_def.dic_function() #get the function dictionary
        if parsed_input[0] in functions:
            func = functions.get(parsed_input[0]) #get the operator and map to its function
            nested = parsed_input[1:] #save the rest of the list
            for i in range(len(nested)):
                #if(isinstance(nested[i], list)): # if the item is a list
                    element = eval(nested[i]) #recursively calculate the result of the nested list
                    nested[i] = element #replace the item with the result
                    #example: [ [- 1 3] [* 2 2]] --> [ -2 4]
            return func(nested)

# def quote_list(parsed_input):
#     print("in quote_list")
#     output = parsed_input[0]
#     for i in range(1, len(parsed_input)):
#         if(isinstance(parsed_input[i], list)):
#             sub_string = quote_list(parsed_input[i])
#             output = output + " " + sub_string
#         else:
#             output = output + " " + str(parsed_input[i])
#     return "(" + output + ")"
#
# def print_quotelist(parsed_input):
#     print("in print_qoutelist")
#     temp = str(quote_list(parsed_input))
#     temp = temp[:-1].split()
#     final = " ".join(temp[1:])
#     print("final: ", final)
#     return final
#
# def render(eval_result):
#     if len(eval_result) == 1:
#         if(eval_result[0].isdigit()):
#             print(int(eval_result[0]))
#         else:
#             result = ''.join(str(eval_result))
#             print(result)
#     if 'QUOTE' in eval_result:
#         print("if has quote")
#         return print_quotelist(eval_result)
#     else:
#         print(eval_result)


def main():
    while True:
        try:
            userInput = raw_input('lispy >') #raw_input return the input as string
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
