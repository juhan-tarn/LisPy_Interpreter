package edu.brynmawr.cs399.blisp.tests;

import static org.junit.jupiter.api.Assertions.*;

import java.io.*;

import org.junit.jupiter.api.*;
import org.junit.jupiter.api.function.*;

import edu.brynmawr.cs399.blisp.builtin.*;
import edu.brynmawr.cs399.blisp.expr.*;
import edu.brynmawr.cs399.blisp.parser.*;

class Eval
{
	private static String eval(String input) throws IOException, ParseErrorException, EvalException
	{
		return Builtins.evalString(input);
	}
	
	private static void assertException(Class<? extends Throwable> cls, Executable e, String msg)
	{
		assertEquals(msg, assertThrows(cls, e).getMessage());
	}
	
	@BeforeAll
	static void loadPreamble() throws IOException, ParseErrorException, EvalException
	{
		try
		{
			Builtins.runPreamble();
		}
		catch(IOException | ParseErrorException | EvalException e)
		{
			e.printStackTrace();
			throw e;
		}
	}
	
	@Test
	void testNumbers() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("3", eval("3"));
		assertEquals("-1", eval("-1"));
		assertEquals("5", eval("+5"));
	}
	
	@Test
	void testArithmetic() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("2", eval("(+ 1 1)"));
		assertEquals("10", eval("(+ 1 2 3 4)"));
		assertEquals("0", eval("(+)"));
		assertEquals("3", eval("(+ 3)"));
		assertEquals("5", eval("(- 5)"));
		assertEquals("3", eval("(- 5 2)"));
		assertEquals("1", eval("(- 5 1 3)"));
		assertEquals("1", eval("(*)"));
		assertEquals("120", eval("(* 1 2 3 4 5)"));
		assertEquals("6", eval("(/ 48 8)"));
		assertEquals("0", eval("(/ 1 2)"));
	}
	
	@Test
	void testNestedArithmetic() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("6", eval("(* 2 (+ 1 2))"));
	}
	
	@Test
	void testBadVariable()
	{
		assertException(EvalException.class, () -> eval("x"), "Unbound symbol: X");
		assertException(EvalException.class, () -> eval("y"), "Unbound symbol: Y");
		assertException(EvalException.class, () -> eval("+"), "Unbound symbol: +");
		assertException(EvalException.class, () -> eval("1+"), "Unbound symbol: 1+");
		assertException(EvalException.class, () -> eval("(+ 1 x)"), "Unbound symbol: X");
	}
	
	@Test
	void testQuote() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("HI", eval("'hi"));
		assertEquals("ARTICHOKE", eval("'Artichoke"));
		assertEquals("19", eval("'19"));
		assertEquals("19", eval("(+ '9 '10)"));
		assertEquals("HI", eval("(quote hi)"));
		assertEquals("(QUOTE HI)", eval("''hi"));
		assertEquals("(1 2 3)", eval("'(1 2 3)"));
		assertEquals("(+ 1 2)", eval("'(+ 1 2)"));
	}
	
	@Test
	void testEvalList()
	{
		assertException(EvalException.class, () -> eval("(1 2 3)"), "Unexpected head of list: 1");
		assertException(EvalException.class, () -> eval("(+ (1 2) 3)"), "Unexpected head of list: 1");
		assertException(EvalException.class, () -> eval("(+ '(1 2) 3)"), "Expecting a number as argument to +: (1 2)");
	}
	
	@Test
	void testList() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("(1 2 3)", eval("(list 1 2 3)"));
		assertEquals("(MY 3 SONS)", eval("(list 'my 3 'sons)"));
		assertEquals("((+ 2 1) 3)", eval("(list '(+ 2 1) (+ 2 1))"));
	}
	
	@Test
	void testNil() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("NIL", eval("()"));
		assertEquals("NIL", eval("nil"));
		assertEquals("NIL", eval("'()"));
	}
	
	@Test
	void testCarCdrCons() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("(A B C D)", eval("(cons 'a '(b c d))"));
		assertEquals("(A B)", eval("(cons 'a (cons 'b nil))"));
		assertEquals("A", eval("(car '(a b c))"));
		assertEquals("(B C)", eval("(cdr '(a b c))"));
		assertEquals("C", eval("(car (cdr (cdr '(a b c d))))"));
	}
	
	@Test
	void testPreds() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("NIL", eval("(null '(a b c))"));
		assertEquals("NIL", eval("(null 5)"));
		assertEquals("NIL", eval("(null (+ 1 2))"));
		assertEquals("T", eval("(null ())"));
		assertEquals("T", eval("(null (cdr '(a)))"));
		assertEquals("T", eval("(listp '(a b c))"));
		assertEquals("T", eval("(listp nil)"));
		assertEquals("T", eval("(listp '(+ 1 2))"));
		assertEquals("NIL", eval("(listp (+ 1 2))"));
		assertEquals("NIL", eval("(listp t)"));
		assertEquals("NIL", eval("(listp 'listp)"));
	}
	
	@Test
	void testIf() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("3", eval("(if (listp '(a b c)) (+ 1 2) (+ 5 6))"));
		assertEquals("11", eval("(if (listp 27) (+ 1 2) (+ 5 6))"));
		assertEquals("NIL", eval("(if (listp 27) (+ 2 3))"));
		assertEquals("5", eval("(if (listp nil) (+ 2 3) x)"));
		assertEquals("5", eval("(if (listp 'x) x (+ 2 3))"));
		assertEquals("3", eval("(and t (+ 1 2))"));
		assertEquals("NIL", eval("(and nil x)"));
		assertEquals("NIL", eval("(or)"));
	}
	
	@Test
	void testPreamble() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("NIL", eval("(not t)"));
		assertEquals("T", eval("(= (+ 2 2) (* 2 2))"));
	}
	
	@Test
	void testDefun() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("OUR-THIRD", eval("(defun our-third (x) (car (cdr (cdr x))))"));
		assertEquals("C", eval("(our-third '(a b c d))"));
		assertEquals("SUM-GREATER", eval("(defun sum-greater (x y z) (> (+ x y) z))"));
		assertEquals("T", eval("(sum-greater 1 4 3)"));
	}
	
	@Test
	void testRecursion() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("OUR-MEMBER", eval("(defun our-member (obj lst)" +
	                                  "  (if (null lst)" +
				                            "    nil" +
	                                  "    (if (equal (car lst) obj)" +
				                            "        lst" +
				                            "        (our-member obj (cdr lst)))))"));
		assertEquals("(B C)", eval("(our-member 'b '(a b c))"));
		assertEquals("NIL", eval("(our-member 'z '(a b c))"));
	}
	
	@Test
	void testLet() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("3", eval("(let ((x 1) (y 2)) (+ x y))"));
		assertEquals("NIL", eval("(let ())"));
		assertEquals("5", eval("(let ((x 5)) x)"));
		assertEquals("8", eval("(let ((x 5) (y 3)) (+ x y))"));
		assertEquals("(A)", eval("(let (tail (b 'a)) (cons b tail))"));
		assertEquals("(A)", eval("(let ((tail) (b 'a)) (cons b tail))"));
		assertEquals("2", eval("(let ((a 5) (b 3)) (let ((a b) (b a)) (- b a)))"));
		assertException(EvalException.class, () -> eval("(progn (let ((x 5)) x) x)"), "Unbound symbol: X");
		assertException(EvalException.class, () -> eval("(let)"), "'let' always requires a variable initializer list");
		assertException(EvalException.class, () -> eval("(let (+ 1 2) (+ 3 4))"), "Initializer in 'let' is an unexpected type: 1");
		assertException(EvalException.class, () -> eval("(let ((x 3 4)) x)"), "Initializer in 'let' has more than 2 elements: (X 3 4)");
	}
	
	@Test
	void testSetq() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("1", eval("(setq a 1)"));
		assertEquals("1", eval("a"));
		assertEquals("3", eval("(setq b 2 c 3)"));
		assertEquals("2", eval("b"));
		assertEquals("3", eval("c"));
		assertEquals("5", eval("(setq d 4 e (+ d 1))"));
		assertEquals("4", eval("d"));
		assertEquals("5", eval("e"));
		assertEquals("7", eval("(setq d 7)"));
		assertEquals("7", eval("d"));
		assertEquals("5", eval("e"));
		assertEquals("10", eval("(let ((a 10)) a)"));
		assertEquals("1", eval("a"));
		assertEquals("15", eval("(let ((a 11)) (setq a (+ a 4)) a)"));
		assertEquals("1", eval("a"));
		assertEquals("17", eval("(let ((a 17)) (setq f 19) a)"));
		assertEquals("1", eval("a"));
		assertEquals("19", eval("f"));
		assertEquals("(1 2 3 7 5 19)", eval("(list a b c d e f)"));
	}
	
	@Test
	void testDo() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("NIL", eval("(do () (t))"));
		assertEquals("5", eval("(do ((x 1 (+ x 1))) ((>= x 5) x))"));
		assertEquals("6", eval("(do ((x 1 (+ x 1))) ((> x 5) x))"));
		assertEquals("10", eval("(setq a 10)"));
		assertEquals("DONE", eval("(do ((x 1 (+ x 1))) ((> x 5) 'done) (setq a (+ 2 a)))"));
		assertEquals("20", eval("a"));
		assertEquals("SNOC", eval("(defun snoc (xs x) (if (null xs) (list x) (cons (car xs) (snoc (cdr xs) x))))"));
		assertEquals("REVERSE", eval("(defun reverse (xs) (if (null xs) nil (snoc (reverse (cdr xs)) (car xs))))"));
		assertEquals("(1 4 9 16)", eval("(do ((lst '(1 2 3 4) (cdr lst)) (res nil (cons (* (car lst) (car lst)) res))) ((null lst) (reverse res)))"));
		assertEquals("NIL", eval("(do ((a 0)) (t))"));
		assertEquals("20", eval("a")); // checking that scopes are clean
	}
	
	@Test
	void testFunction() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("#<SYSTEM-FUNCTION +>", eval("(function +)"));
		assertEquals("#<SYSTEM-FUNCTION progn>", eval("(function progn)"));
		assertException(EvalException.class, () -> eval("(function let)"), "LET is a special form, not a function.");
		assertEquals("#<user-defined function>", eval("#'not"));
		assertEquals("#<SYSTEM-FUNCTION null>", eval("#'null"));
		assertEquals("#<user-defined function>", eval("#'(lambda (x y) (+ x y))"));
	}
	
	@Test
	void testApply() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("6", eval("(apply #'+ '(1 2 3))"));
		assertEquals("6", eval("(apply '+ '(1 2 3))"));
		assertEquals("7", eval("(apply #'(lambda (x y) (+ x (* 2 y))) '(3 2))"));
	}
	
	@Test
	void testMap() throws IOException, ParseErrorException, EvalException
	{
		assertEquals("MAPCAR", eval("(defun mapcar (f xs) (if (null xs) nil (cons (apply f (list (car xs))) (mapcar f (cdr xs)))))"));
		assertEquals("1+", eval("(defun 1+ (x) (+ x 1))"));
		assertEquals("SQUARE", eval("(defun square (x) (* x x))"));
		assertEquals("(2 3 4)", eval("(mapcar #'1+ '(1 2 3))"));
		assertEquals("(1 4 9)", eval("(mapcar #'square '(1 2 3))"));
		assertEquals("COMPOSE", eval("(defun compose (f1 f2) #'(lambda (x) (apply f1 (list (apply f2 (list x))))))"));
		assertEquals("(2 5 10)", eval("(mapcar (compose #'1+ #'square) '(1 2 3))"));
		assertEquals("(4 9 16)", eval("(mapcar (compose #'square #'1+) '(1 2 3))"));
	}
}
