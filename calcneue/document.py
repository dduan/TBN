from calcneue.parser import CalcNeueParser
from calcneue.reduce import reduce
from calcneue.reduce_unit import unit_is_complex, unit_is_empty
from calcneue.convert import convert
import math
class Document:
    def __init__(self, body):
        self.lines = body.split('\n')
        self.context = {
                'variables': {
                'PI': (math.pi, (set(), set())),
                'pi': (math.pi, (set(), set())),
                'e': (math.e, (set(), set()))
                },
                'current_unit': None,
                'current_base_unit': None,
                }
        self.calc = CalcNeueParser()
        self.is_currency = False
    
    def evaluate(self):
        final = []
        for l in self.lines:
            try:
                reduced = reduce(self.context, self.calc.parser.parse(l))
                if not unit_is_complex(reduced[1]):
                    if unit_is_empty(reduced[1]):
                        reduced = convert((reduced[0], None), self.context['current_unit'])
                    else:
                        unit = tuple(reduced[1][0])[0][0]
                        reduced = convert((reduced[0], unit), self.context['current_unit'])
                        # round to second decimal place for currency
                        if self.context["current_base_unit"] == ({('EURO', 1)}, set()):
                            reduced = (round(reduced[0], 2), reduced[1])
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
