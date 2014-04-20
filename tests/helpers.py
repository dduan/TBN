def _i(i, unit=None): return 'quantity', ('integer_number', i), unit
def _f(f, unit=None): return 'quantity', ('float_number', f), unit
def input_should_match(test, fixtures):
    for input, target in fixtures.items():
        assert test(input) == target

def _sunit(unit=None):
    if not unit:
        return (set(), set())
    else:
        return ({(unit, 1), }, set())

def _almost_equal(a, b, threshold=0.0001):
    ''' test float number equality'''
    return  a - b < threshold
