
# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, DIVIDE, MULTIPLY, EOF = 'INTEGER', 'PLUS', 'MINUS', 'DIVIDE', 'MULTIPLY', 'EOF'


class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = text
        
        # self.pos is an index into self.text
        self.pos = 0
        
        # current token instance
        self.current_token = None
        
        #current character by position in the input stream
        self.current_char = self.text[self.pos]
        
    def error(self):
        raise Exception('Error parsing input')

    def endofstring(self):
        if (self.pos+1) > (len(self.text)-1):
            return True
        else:
            return False
            
    def get_next_token(self):
        number = None
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        #text = self.text

        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > (len(self.text) - 1):
            return Token(EOF, None)
        
        # get a character at the position self.pos and decide
        # what token to create based on the single character
        #current_char = self.text[self.pos]

        while (self.current_char == " "):
            if(self.endofstring()):
                return Token(EOF, None)
            else:
                self.pos+=1
                self.current_char = self.text[self.pos]
                
        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        
        #if current_char.isdigit():
        #    token = Token(INTEGER, int(current_char))
        #    self.pos += 1
        #    return token
        if self.current_char.isdigit():
            while self.current_char.isdigit():
                if number == None:
                    number = self.current_char
                else:
                    number += self.current_char
                if(self.endofstring()):
                    break
                else:
                    self.pos+=1
                self.current_char = self.text[self.pos]
        
        if number != None:
            token = Token(INTEGER, int(number))
            return token
            
        if self.current_char == '+':
            token = Token(PLUS, self.current_char)
            self.pos += 1
            return token
            
        if self.current_char == '-':
            token = Token(MINUS, self.current_char)
            self.pos +=1
            
        if self.current_char == '/':
            token = Token(DIVIDE, self.current_char)
            self.pos +=1

        if self.current_char == '*':
            token = Token(MULTIPLY, self.current_char)
            self.pos +=1

        self.error()
        
    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        # we expect the current token to be a single-digit integer
        #left = self.current_token
        #self.eat(INTEGER)

        # we expect the current token to be a '+' token
        #op = self.current_token
        #self.eat(PLUS)

        # we expect the current token to be a single-digit integer
        #right = self.current_token
        #self.eat(INTEGER)
        # after the above call the self.current_token is set to
        # EOF token

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
        #result = left.value + right.value
        
        left = self.current_token
        self.eat(left.type)
        
        op = self.current_token
        print("Left token: " + op.value)
        self.eat(op.type)
        
        right = self.current_token
        print("Right token: " + right.value)
        self.eat(right.type)
        
        if(op.type == PLUS):
            print("Left value: " + str(left.value) + "Right value: " + str(right.value))
            result = left.value + right.value # eval(left.value + op.value + right.value) #
        
        if(op.type == MINUS):
            result = left.value - right.value # eval(left.value + op.value + right.value) #

        if(op.type == DIVIDE):
            if(right.value == 0):
                print("Divide by zero not allowed")
                result = None #Cannot divide by zero
                
        if(op.type == MULTIPLY):
            result = left.value * right.value # eval(left.value + op.value + right.value) #
        
        return int(result)
            

def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
