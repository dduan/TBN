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

def unit_multiply(a, b):
    "if there's common (unit, degree) pair, double the degree before merge"
    common_nu = a[0].intersection(b[0])
    nu = set()
    for u, deg in common_nu:
        nu.add((u, deg * 2))
    nu = nu.union(a[0].symmetric_difference(b[0]))

    common_de = a[1].intersection(b[1])
    de = set()
    for u, deg in common_de:
        de.add((u, deg * 2))
    de = de.union(a[1].symmetric_difference(b[1]))
    return simplify_unit((nu, de))

def unit_divide(a, b):
    "same as multiply except b's nu and de are swapped"
    "if there's common (unit, degree) pair, double the degree before merge"
    common_nu = a[0].intersection(b[1])
    nu = set()
    for u, deg in common_nu:
        nu.add((u, deg * 2))
    nu = nu.union(a[0].symmetric_difference(b[1]))

    common_de = a[1].intersection(b[0])
    de = set()
    for u, deg in common_de:
        de.add((u, deg * 2))
    de = de.union(a[1].symmetric_difference(b[0]))
    return simplify_unit((nu, de))

def unit_power(unit, power):
    "take unit to a power"
    result = (set(), set())

    [result[0].add((u[0], u[1] * power)) for u in unit[0]]
    [result[1].add((u[0], u[1] * power)) for u in unit[1]]

    return result
