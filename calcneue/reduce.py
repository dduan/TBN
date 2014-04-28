import math
try:
    from calcneue.convert import convert, lookup_alias, convert_to_base, simple_unit_from_complex_unit
    from calcneue.reduce_unit import *
except ImportError:
    from convert import convert, lookup_alias, convert_to_base, simple_unit_from_complex_unit
    from reduce_unit import *

# TODO:
# use unknown units
def reduce(context, node):
    print(node)
    return globals()['reduce_' + node[0]](context, *node[1:])

def reduce_quantity(context, number, unit):
    result = convert_to_base(number[1], lookup_alias(unit))
    context['current_unit'] = unit
    context['current_base_unit'] = result[1]
    return result

def reduce_convert_expr(context, expr, unit):
    ''' expr in unit '''
    result = None
    expr = reduce(context, expr)
    context['current_base_unit'] = expr[1]
    if unit_is_complex(expr[1]):
        result = reduce(context, expr)
    elif not unit_is_empty(expr[1]): # 1 km in m
        result = convert((expr[0], list(expr[1][0])[0][0]), unit)
    else:
        result = convert((expr[0], None), unit)

    context['current_unit'] = unit
    return result

def reduce_assignment(context, expr, name):
    context['current_unit'] = simple_unit_from_complex_unit(expr)
    val = reduce(context, expr)
    context["variables"][name] = convert(
        (val[0], simple_unit_from_complex_unit(val)),
        context['current_unit'])
    return val

def reduce_binop_plus(context, left, right):
    lval = reduce(context, left)
    rval = reduce(context, right)
    if (unit_is_equal(lval[1], rval[1])):
        return lval[0] + rval[0], rval[1]
    elif (unit_is_empty(lval[1])):
        return lval[0] + rval[0], rval[1]
    elif (unit_is_empty(rval[1])):
        return lval[0] + rval[0], lval[1]
    else:
        return (None, (set(), set()))

def reduce_binop_minus(context, left, right):
    lval = reduce(context, left)
    rval = reduce(context, right)
    if (unit_is_equal(lval[1], rval[1])):
        return lval[0] - rval[0], rval[1]
    elif (unit_is_empty(lval[1])):
        return lval[0] - rval[0], rval[1]
    elif (unit_is_empty(rval[1])):
        return lval[0] - rval[0], lval[1]
    else:
        return (None, (set(), set()))

def reduce_binop_multiply(context, left, right):
    lval = reduce(context, left)
    rval = reduce(context, right)
    unit = unit_multiply(lval[1], rval[1])
    return lval[0] * rval[0], unit

def reduce_binop_divide(context, left, right):
    lval = reduce(context, left)
    rval = reduce(context, right)
    unit = unit_divide(lval[1], rval[1])
    return lval[0] / rval[0], unit

def reduce_binop_mod(context, left, right):
    lval = reduce(context, left)
    rval = reduce(context, right)
    unit = unit_divide(lval[1], rval[1])
    return lval[0] % rval[0], unit

def reduce_binop_power(context, left, right):
    lval = reduce(context, left)
    rval = reduce(context, right)
    if unit_is_empty(rval[1]):
        return lval[0] ** rval[0], unit_power(lval[1], rval[0]) 
    else:
        return (None, (set(), set()))

def reduce_function_expr(context, params, funcname):
    func = getattr(math, funcname, None)
    val, unit = reduce(context, params)
    if not func: return None, (set(), set())
    return func(val), unit


def reduce_variable(context, name, unit):
    ''' add unit only when variable had no unit previously'''
    val = context["variables"].get(name, None)
    if val:
        context['current_unit'] = simple_unit_from_complex_unit(val)
    if val and unit_is_empty(val[1]) and unit:
        return val[0], ({(unit, 1)}, set())
    elif val and not unit:
        return val
    else:
        return None, (set(), set())

def reduce_negative_expr(context, expr):
    expr = reduce(context, expr)
    return ((-expr[0], expr[1]))

if __name__ == '__main__':
    from calcneue.parser import CalcNeueParser
    calc = CalcNeueParser()
    while True:
        try:
            s = input('reduce > ')
        except EOFError:
            break
        print(reduce({}, calc.parser.parse(s)))
