from calcneue.parser import CalcNeueParser
from calcneue.reduce import reduce
class Document:
    def __init__(self, body):
        self.lines = body.split('\n')
        self.context = {}
        self.calc = CalcNeueParser()
    
    def evaluate(self):
        final = []
    	for l in self.lines:
        	try:
        		reduced = self.beautify(reduce(self.context, self.calc.parser.parse(l)))

        	except:
        		reduced = None
        	if reduced == None:
        		reduced = ''

    		final.append(reduced)
    	return final

    def beautify(self, expr):
    	'''make the unit look better'''
    	print(expr)
    	num, unit = expr
    	def simplify(units):
    		result = []
    		for u in units:
    			if u[1] == 1:
    				result.append('{}'.format(u[0]	))
    			else:
    				result.append('{}^{}'.format(u[0], u[1]))
    		return ' * '.join(result)


    	nu_str = simplify(unit[0])
    	de_str = simplify(unit[1])

    	if de_str:
    		return '{} {} / {}'.format(num, nu_str, de_str)
    	else:
    		return '{} {}'.format(num, nu_str)
