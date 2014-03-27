import pytest
from calcneue.lexer import CalcNeueLexer

@pytest.fixture(scope="module")
def calc():
    return CalcNeueLexer()

def test_literals(calc):
    #calc = CalcNeueLexer()
    literals = r'-()+*/%^='
    calc.lexer.input(literals)
    for i, t in enumerate(calc.lexer):
        assert t.type == literals[i]
        assert t.value == literals[i]
        assert t.lineno == 1
        assert t.lexpos == i

def test_in(calc):
    calc.lexer.input('in')
    t = [tok for tok in calc.lexer][0]
        #assert tok.type == 'IN'
        #assert tok.value == 'in'
    assert t.type == 'IN'
    assert t.value == 'in'

def test_integer(calc):
    ints = {
        '1': 10,
        '0': 10, 
        '0b1101': 2,
        '0B01': 2,
        '0xA': 16,
        '0X1B': 16,
        '0o7': 8,
        '0o11': 8
    }
    keys = list(ints.keys())
    calc.lexer.input(' '.join(keys))
    for i, tok in enumerate(calc.lexer):
        assert tok.type == 'INTEGER'
        assert tok.value == int(keys[i], ints[keys[i]])

def test_float(calc):
    floats = [
        '1.0',
        '3.14159',
        '3e2',
        '22E-2'
    ]
    calc.lexer.input(' '.join(floats))
    for i, tok in enumerate(calc.lexer):
        assert tok.type == 'FLOAT'
        assert tok.value == float(floats[i])

def test_identifiers(calc):
    ids = ['winter', 'is', 'coming']
    calc.lexer.input(' '.join(ids))
    for i, tok in enumerate(calc.lexer):
        assert tok.type == 'IDENTIFIER'
        assert tok.value == ids[i]

