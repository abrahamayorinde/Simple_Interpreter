# Simple_Interpreter
Building a Simple Interpreter according to https://ruslanspivak.com/lsbasi-part1/

Motivation:
Abstract Syntax Tree

This is my first attempt at creating an abstract syntax tree.  My interest in the subject developed in a roundabout way.

Initially, I wanted to create something to assist me with mastering Control Systems. The subject requires some understanding of the Routh-Hurwitz stability criterion. Control systems can typically be represented by a polynomial after some processing via the laplace transform. Stability is determined by arranging the coefficients of the polynomial in a particular way and applying a sequence of arithmetic operations (Routh-Hurwitz).

I wanted to see if there was a public online tool that helps one simply plug in the coefficients, both literals and variables, to arrive at an answer but I didn't find any though they may be out there.

So I figured I would write one. Implementing the arithmetic operations by hand is really rather simple, however utilizing a computer to come to the same output is not trivial. I discovered the end of my knowledge when it came to using variables as coefficients instead of numeric values.

After doing many web searches, including terms such as 'parsing', 'processing', 'make my program do math', 'arbitrary length', I eventually stumbled upon the solution 'abstract syntax tree'.

Delving into this topic will reveal to me how to complete the problem.  The solution to this problem also extends into programming languages themselves and my limited knowledge of the inner workings of compilation and compilers. 

"If you don't know how compilers work, then you don't understand computers." While I knew what a compiler does, exactly how it worked, I hadn't the foggiest (idea).

Now I sort of do, but by the end of this journey I absolutely will.

Thank you. AOA.
