# Simple_Interpreter
Building a Simple Interpreter according to https://ruslanspivak.com/lsbasi-part1/

Interpreter #2:
This lessons is supposed to add the following functionality:
    1. Handle whitespace characters anywhere in the input string
    2. Consume multi-digit integers from the input
    3. Subtract two integers (currently it can only add integers)
    
I already jumped ahead and added 2 and 3 in the first lesson so never mind that.  So only 1 is added in this lesson.

The function 'endofstring' was changed to lastcharacter.  Another function will now track the position in the text being processed while this determines if the end of the string input has been reached.

The function 'nextchar' that advances the position in the text was added. This function takes over the funcitonality that was in each of the branches of 'get_next_token'.

The functionality of capturing a number was separated into its own function,  and is now called from 'getnumber' in 'get_next_token'.

Interpreter #1:
This first lesson is pretty straight forward. 

The python code is broken into several 'sections';  string literals, two classes and the main function.  

The string literals are used to identify the various types of objects that will be in our stream input to our simiple interpreter.  This number of literals will grow as the program grows to include more operations, symbols, etc.  

The classes are currently an Interpreter and Token class.
The input stream of the interpreter must tokenize the various symbols that will be part of the input stream.  Each token has a type and corresponding value.  The token class will hold this information (Token{type, value}).
The Interpeter class will do the process the input stream as token and produce an output.  It has four member variables; the input text {text}, the current position in the text {pos}, the current character being processed {current_char}, and the current token from the input stream {current_token}.

In addition to the init function, there other functions are; error, endofstring, get_next_token, eat, expression.
error serves to notify that the input was malformed or invalid.
'endofstring' keeps track of the current character position of the input text.
'get_next_token' processes the input symbols as tokens.
'eat' processes one token to the next.
'expression' will actually use the token values to produce an algebraic output.

This implementation can only handle simple algebraic functions without precedence ~~and numbers of single digits only~~.

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
