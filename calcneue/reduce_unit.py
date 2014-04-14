'''
internal representation of a unit during reduce:
	(
	[(unit, deg), (unit,deg), ...], # list of numerators
	[(unit, deg), (unit,deg), ...]  # list of denominators
	)
'''
def unit_is_empty(unit):
    ''' empty or None'''
    pass

def unit_is_equal(a, b):
    pass

def simplify_unit(unit):
    pass

def unit_is_complex(unit):
    ''' numerator has one unit with degree 1, denominator is empty'''
    return len(unit[0]) == 1 and unit[0][1] == 1 and len(unit[2]) == 0
