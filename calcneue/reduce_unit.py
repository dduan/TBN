'''
internal representation of a unit during reduce:
	(
	[(unit, deg), (unit,deg), ...], # list of numerators
	[(unit, deg), (unit,deg), ...]  # list of denominators
	)
'''
def unit_is_empty(unit):
    ''' empty or None'''
    return unit==([], [])

def unit_is_equal(a, b):
    return a==b

def simplify_unit(unit):
    pass

def unit_is_complex(unit):
    ''' numerator has one unit with degree 1, denominator is empty'''
    #print(len(unit[0]))
    #print(len(unit[1]))
    #print(unit[0][0][1])
    if len(unit[0]) == 1 and unit[0][0][1] == 1 and len(unit[1]) == 1 and len(unit[1][0]) == 0:
        print("unit is complex")
        return True
