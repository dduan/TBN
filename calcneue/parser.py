from __future__ import print_function, unicode_literals, division

import ply.yacc as yacc
# TODO: return None for invaild input
try:
    from calcneue.lexer import CalcNeueLexer
except:
        from lexer import CalcNeueLexer

class CalcNeueParser:

    precedence = (
        ('left', '='),
        ('left', '+', '-'),
        ('left', '*', '/', '%'),
        ('right', '^'),
        ('right', 'UMINUS'),
    )

    def __init__(self):
        self.lexer = CalcNeueLexer()
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self)


    def p_binop_plus(self, p):
        'expression   : expression "+" expression'
        p[0] = ('binop_plus', p[1], p[3])

    def p_binop_minus(self, p):
        'expression   : expression "-" expression'
        p[0] = ('binop_minus', p[1], p[3])

    def p_binop_multiply(self, p):
        'expression   : expression "*" expression'
        p[0] = ('binop_multiply', p[1], p[3])

    def p_binop_divide(self, p):
        'expression   : expression "/" expression'
        p[0] = ('binop_divide', p[1], p[3])

    def p_binop_mod(self, p):
        'expression   : expression "%" expression'
        p[0] = ('binop_mod', p[1], p[3])

    def p_binop_power(self, p):
        'expression   : expression "^" expression'
        p[0] = ('binop_power', p[1], p[3])

    def p_expression_paren(self, p):
        '''expression   : "(" expression ")"'''
        #p[0] = ('group_expr', p[2])
        p[0] = p[2]

    def p_assignment(self, p):
        "expression :   IDENTIFIER '=' expression"
        p[0] = ('assignment', p[3], p[1])

    def p_negative_expr(self, p):
        "expression :   - expression %prec UMINUS"
        p[0] = ('negative_expr', p[2])

    def p_expression_unit_convert(self, p):
        '''expression   :   expression IN IDENTIFIER'''
        p[0] = ('convert_expr', p[1], p[3])

    def p_expression_function(self, p):
        "expression     :   IDENTIFIER '(' expression ')' "
        p[0] = ('function_expr', p[3], p[1])

    def p_expression_quantity(self, p):
        '''expression   :   number IDENTIFIER
                        |   number'''
        try:
            p[0] = ('quantity', p[1], p[2])
        except IndexError:
            p[0] = ('quantity', p[1], None)

    def p_number_float(self, p):
        '''number : FLOAT'''
        p[0] = ('float_number', p[1])

    def p_number_integer(self, p):
        '''number : INTEGER'''
        p[0] = ('integer_number', p[1])

    def p_error(self, p):
        print("syntax error: {}".format(p))

if __name__ == '__main__':
    calc = CalcNeueParser()
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        print(calc.parser.parse(s))
