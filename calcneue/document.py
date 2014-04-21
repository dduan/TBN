from calcneue.parser import CalcNeueParser
from calcneue.reduce import reduce
class Document:
    def __init__(self, body):
        self.lines = body.split('\n')
        self.context = {}
        self.calc = CalcNeueParser()
    
    def evaluate(self):
        return [str(reduce(self.context, self.calc.parser.parse(l))) for l in self.lines]
