Symbol = str          # A Lisp Symbol is implemented as a Python str
List   = list         # A Lisp List   is implemented as a Python list
Number = (int, float) # A Lisp Number is implemented as a Python int or float



# def parse(program):
#     "Read a Scheme expression from a string."
#     return read_from_tokens(tokenize(program))
#
# def tokenize(s):
#     "Convert a string into a list of tokens."
#     return s.replace('(',' ( ').replace(')',' ) ').split()
#
# def read_from_tokens(tokens):
#     "Read an expression from a sequence of tokens."
#     if len(tokens) == 0:
#         raise SyntaxError('unexpected EOF while reading')
#     token = tokens.pop(0)
#     if '(' == token:
#         L = []
#         while tokens[0] != ')':
#             L.append(read_from_tokens(tokens))
#         tokens.pop(0) # pop off ')'
#         return L
#     elif ')' == token:
#         raise SyntaxError('unexpected )')
#     else:
#         return atom(token)
#
# def atom(token):
#     "Numbers become numbers; every other token is a symbol."
#     try: return int(token)
#     except ValueError:
#         try: return float(token)
#         except ValueError:
#             return Symbol(token)
#
# def repl(prompt='lis.py> '):
#     "A prompt-read-eval-print loop."
#     while True:
#         val = eval(parse(input(prompt)))
#         if val is not None:
#             print(lispstr(val))
#
# def lispstr(exp):
#     "Convert a Python object back into a Lisp-readable string."
#     if isinstance(exp, List):
#         return '(' + ' '.join(map(lispstr, exp)) + ')'
#     else:
#         return str(exp)
#
# def main():
#     while True:
#         try:
#             userInput = raw_input('lispy >') #raw_input return the input as string
#         except EOFError:
#             break
#         if not userInput:
#             continue
#         print(tokenize(userInput))

if __name__ == '__main__':
    print(int(3))
    print(Symbol(["hi"]))
