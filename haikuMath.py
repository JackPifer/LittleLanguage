from lark import Lark, Transformer, v_args

grammar = """
    ?start: expr
    ?expr: term
          | expr "add these together" term -> add
          | expr "add these two terms together" term -> add
          | expr "subtract this term from the first" term -> sub
          | expr "subtract these two terms" term -> sub
          
    ?term: factor
          | term "multiply the terms" factor -> mul
          | term "multiply these two numbers" factor -> mul
          | term "divide by the next number" factor -> div
          | term "divide these two terms" factor -> div
    ?factor: NUMBER -> number
           | "open the parentheses" expr "now we close parentheses"
           
    %import common.NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""
'''
grammar ="""
    ?start: expr
    ?expr: term
          | expr "add these two terms together" -> add
          | expr "subtract this term from the first" -> sub
    ?term: factor
          | term "multiply the term" factor -> mul
          | term "divide by the next number" factor -> div
    ?factor: NUMBER -> number
           | "open the parentheses" expr "now we close parentheses"
           
    %import common.NUMBER
    %import common.WS_INLINE
    %ignore WS_INLINE
"""
'''

class ArithmeticTransformer(Transformer):
    @v_args(inline=True)
    def add(self, a, b):
        return a + b

    @v_args(inline=True)
    def sub(self, a, b):
        return a - b

    @v_args(inline=True)
    def mul(self, a, b):
        return a * b

    @v_args(inline=True)
    def div(self, a, b):
        return a / b

    def number(self, n):
        return float(n[0])

def evaluate(expression):
    parser = Lark(grammar, parser='lalr', transformer=ArithmeticTransformer())
    return parser.parse(expression)

# Example usage:
#expression = "3 * (4 + 5) - 6 / 2"
#expression = "4 + 5"
expression = input("Enter your equation ")
#expression = "3 add these two terms together 5"
#expression = "3 add these together 5"
#expression = "3 subtract this term from the first 5"
#expression = "3 multiply the term open the parentheses 4 add these two terms together 5 now we close parentheses subtract this term from the first 6 divide by the next number 2"
result = evaluate(expression)
print(expression, "=", result)  # Output: 3 * (4 + 5) - 6 / 2 = 24.0