from sympy.logic import simplify_logic as parser
import re

def lexer(expression):
    tokens = []  # store tokens
    position = 0  # position a variable to 0
    operators = {'+', '|', '*', '&', '!', '~', '(', ')'}  # set of operators
    while position < len(expression):  # loop that runs until position is less than the length of the expression
        char = expression[position]  # get character at current position
        if char == ' ':  # check if char = space
            position += 1  # If it is, move 
        elif char.isalpha():  # check if char is alphabet
            var_name = ''  # store variable name
            while position < len(expression) and expression[position].isalpha():  # loop that runs while the position is within the expression and the character at the position is alphabetic
                var_name += expression[position]  # add character to var_name
                position += 1  # move
            tokens.append(var_name)  # add var name to token list
        elif char in operators:  # Check if the character is in the set of operators
            tokens.append(char)  # add to token list
            position += 1  # move
        else:
            raise ValueError(f"Unexpected character: {char}")

    return tokens

def custom_parser(tokens):
    # Convert tokens list to a string
    expression_str = ''.join(tokens)

    # Replace '|' with '+' and '&' with '*' for sympy parsing
    expression_str = re.sub(r'\|', '+', expression_str)
    expression_str = re.sub(r'&', '*', expression_str)
    expression_str = re.sub(r'~', '!', expression_str)

    return expression_str

example_expression = input("Enter the Boolean Expression: ")
tokens = lexer(example_expression)

print("LEXER: ", tokens)
print(custom_parser(tokens))
print("SIMPLIFIED: ", parser(example_expression))
