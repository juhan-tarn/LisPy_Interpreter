#A Clisp interpreter
#
import re
import function_def
Symbol = str          # A Lisp Symbol is implemented as a Python str
List = list
Num = int

 ##evaluation on variables should just be error for now
 ## numbers evaluate to themselves
 ## for list, the first thing is always the funciton
def tokenize(chars):
    "Convert a string of characters into a list of tokens."
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def read_from_tokens(tokens):
    "Read an expression from a sequence of tokens."
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')
    token = tokens.pop(0)
    if '(' == token:
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif ')' == token:
        raise SyntaxError('unexpected )')
    else:
        return atom(token)


def atom(token):
    "Numbers become numbers; every other token is a symbol."
    try: return int(token)
    except ValueError:
        return Symbol(token)

def parse(program):
    "Read a Scheme expression from a string."
    return read_from_tokens(tokenize(program))

def is_balanced(input):
    "Check if an expression has matching parentheses"
    sum = 0
    for i in range(len(input)):
        if sum < 0: #ensure that ) doesn't go first
            return False
        if input[i] == '(':
            sum = sum + 1
        elif input[i] == ')':
            sum = sum - 1
    if sum == 0:
        return True
    else:
        return False

def eval(parsed_input):
    try: return int(parsed_input)
    except:
        functions = function_def.dic_function()
        if parsed_input[0] in functions:
            Value_ = functions.get(parsed_input[0])
            nested = parsed_input[1:]
            for i in range(len(nested)):
                if(isinstance(nested[i], list)):
                    element = eval(nested[i])
                    nested[i] = element

            #print(Value_(nested))
            return Value_(nested)

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
            print("not enough parentheses, try again")
            #raise SyntaxError('unmatching pairs of parentheses')
            continue
        elif is_balanced(userInput) == True:
            #print("enough parentheses")
            print(eval(parse(userInput)))


if __name__ == '__main__':
    main()
