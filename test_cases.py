'''
Test cases taken from Richard's Java eval file
'''
import lispy_interpreter as li


def arithmetic_test():
    assert (li.eval(li.parse("(/ 1 2)"))) == 0
    assert (li.eval(li.parse("(+ 1 1)"))) == 2
    assert (li.eval(li.parse("(+ 1 2 3 4)"))) == 10
    assert (li.eval(li.parse("(+)"))) == 0
    assert (li.eval(li.parse("(+ 3)"))) == 3
    assert (li.eval(li.parse("(- 5)"))) == 5
    assert (li.eval(li.parse("(- 5 2)"))) == 3
    assert (li.eval(li.parse("(- 5 1 3)"))) == 1
    assert (li.eval(li.parse("(*)"))) == 1
    assert (li.eval(li.parse("(* 1 2 3 4 5)"))) == 120
    assert (li.eval(li.parse("(/ 48 8)"))) == 6
    assert (li.eval(li.parse("(/ 1 2)"))) == 0
    assert (li.eval(li.parse("(* 2 (+ 1 2))"))) == 6
    assert (li.eval(li.parse("(+ (* 1 2) (/ 6 3) +2 -2 )"))) == 4
    #if nothing shows up when running the above test cases, then all test cases are passed

arithmetic_test()    
