'''
internal representation of a unit during reduce:
    (
    {(unit, deg), (unit,deg), ...}, # set of numerators
    {(unit, deg), (unit,deg), ...}  # set of denominators
    )
'''
def unit_is_empty(unit):
    ''' empty or None'''
    return unit == (set(), set())

def unit_is_equal(a, b):
    return simplify_unit(a) == simplify_unit(b)

def simplify_unit(unit):
    count = {}
    result = (set(), set())
    for u, deg in unit[0]:
        count[u] = count.get(u, 0) + deg
    for u, deg in unit[1]:
        count[u] = count.get(u, 0) - deg
    for u, deg in count.items():
        if deg > 0: result[0].add((u, deg))
        if deg < 0: result[1].add((u, -deg))
    return result


def unit_is_complex(unit):
    '''not (numerator has one unit with degree 1, denominator is empty)'''
    simple = len(unit[0]) == 1 and list(unit[0])[0][1] == 1 and not len(unit[1])
    return not simple and not unit_is_empty(unit)
