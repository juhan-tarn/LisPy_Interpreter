# LisPy_Interpreter <br/>

An interpreter in Python for Lisp.
<br/>So far the interpreter can evaluate _arithmetic expressions, including nested expressions._

This interpreter works in Python 3.4, and it contains regular expression package (regular expression is built-in). If regular expression package cannot be imported, try `pip install regex`

To run this interpreter:
- download Python (preferably version 3.4)
- download the interpreter files on this github
- execute `python lispy_interpreter.py` at the path of the files in terminal
   - You'll see `lispy > ` appear!
- Input `Quit` or `control-C` to terminate the interpreter.

To run the test cases:
- execute `python test_cases.py`
   - if nothing shows up in the terminal, then all test cases are passed.

REPL is not correctly implemented, when user types not matching parentheses and press Enter, the interpreter would not "wait" for the user to complete the parentheses, instead, the interpreter would start a new prompt
