from calcneue.parser import CalcNeueParser
from calcneue.reduce import reduce
from calcneue.reduce_unit import unit_is_complex
from calcneue.convert import convert
class Document:
    def __init__(self, body):
        self.lines = body.split('\n')
        self.context = {
                'variables': {},
                'current_unit': None
                }
        self.calc = CalcNeueParser()
    
    def evaluate(self):
        final = []
        for l in self.lines:
            try:
                reduced = reduce(self.context, self.calc.parser.parse(l))
                if not unit_is_complex(reduced[1]):
                    reduced = convert((reduced[0], tuple(reduced[1][0])[0][0]), self.context['current_unit'])
                reduced = self.beautify(reduced)
            except:
                print("something is wrong!!")
                reduced = None
            if reduced == None:
                reduced = ''

            final.append(reduced)
        return final

    def beautify(self, expr):
        '''make the unit look better'''
        num, unit = expr
        def simplify(units):
            result = []
            for u in units:
                if u[1] == 1:
                    result.append('{}'.format(u[0]  ))
                else:
                    result.append('{}^{}'.format(u[0], u[1]))
            return ' * '.join(result)


        nu_str = simplify(unit[0])
        de_str = simplify(unit[1])

        if de_str:
            return '{} {} / {}'.format(num, nu_str, de_str)
        else:
            return '{} {}'.format(num, nu_str)
