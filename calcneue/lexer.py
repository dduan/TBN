from __future__ import print_function, unicode_literals, division

import ply.lex as lex

class CalcNeueLexer:
    def __init__(self):
        self.lexer = lex.lex(module=self)

    reserved = {
        'in': "IN"
    }
    literals = r'-()+*/%^='
    tokens = [
        'INTEGER',
        'FLOAT',
        'IDENTIFIER'

    ] + list(reserved.values())

    # identifiers
    #remember to escape '-' in the literals
    @lex.TOKEN(r'[^0-9\-'+literals[1:]+']\w*')
    def t_IDENTIFIER(self, t):
        t.type = self.reserved.get(t.value, 'IDENTIFIER')
        return t

    # float
    re_float_point = r'([0-9]*\.[0-9]+|[0-9]+\.)'
    re_float_exponent = r'([0-9]+|'+ re_float_point + r')[eE][+-]?[0-9]+'
    @lex.TOKEN(r'({}|{})'.format(re_float_point, re_float_exponent))
    def t_FLOAT(self, t):
        t.value = float(t.value)
        return t

    # integer
    re_integers = (
        r'0(x|X)[0-9a-fA-F]+',  #hexadecimal
        r'0(o|O)[0-7]+',        #octal
        r'0(b|B)[01]+',         #binary
        r'[1-9][0-9]*',         #decimal
        r'0'                    #zero
    )
    re_integer = '(' + ')|('.join(re_integers) + ')'

    @lex.TOKEN(re_integer)
    def t_INTEGER(self, t):
        if len(t.value) > 1 and t.value[0] == '0': # non-decimal
            base = {
                'b': 2, 'B': 2,
                'x': 16, 'X': 16,
                'o': 8, 'O': 8
            }.get(t.value[1])
        else:
            base = 10
        t.value = int(t.value, base)
        return t


    # the rest
    t_ignore = ' \t'

    def t_error(self, t):
        print('Lexing Error: {}'.format(t))
        t.lexer.skip(1)

if __name__ == '__main__':
    lexer = CalcNeueLexer()
    while True:
        try:
            lexer.lexer.input(input('tokenize > '))
        except EOFError:
            break
        for tok in lexer.lexer:
            print(tok)
