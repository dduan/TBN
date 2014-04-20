from __future__ import print_function, unicode_literals, division
from calcneue.convert import convert, lookup_base_unit
from calcneue.reduce_unit import *

# TODO:
# variables
# use unknown units
# tolerate partial errors 
def reduce(context, node):
    return globals()['reduce_' + node[0]](context, *node[1:])

def reduce_quantity(context, number, unit):
    baseunit = lookup_base_unit(unit)
    #print(number)
    print("calling convert from reduce_quantity")
    return convert((number[1], unit), baseunit)

def reduce_convert_expr(context, expr, unit):
    expr = reduce(context, expr)
    if unit_is_complex(expr[1]):
        return reduce(context, expr)
    elif not unit_is_empty(expr[1]):
        print("calling convert from reduce_convert_quantity")
        return convert((expr[0], expr[1][0][0][0]), unit)
    else:
        return convert((expr[0], None), unit)

def reduce_assignment(context, expr, id):
    #TODO: implement side effects aka register id
    return reduce(context, expr)

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
        return (None, ([], []))

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
        return (None, ([], []))

def reduce_binop_multiply(context, left, right):
    lval = reduce(context, left)
    rval = reduce(context, right)
    unit = simplity_unit((lval[1][0]+rval[1][0], lval[1][1]+rval[1][1]))
    return lval[0] * rval[0], unit

def reduce_binop_divide(context, left, right):
    lval = reduce(context, left)
    rval = reduce(context, right)
    unit = simplity_unit((lval[1][0]+rval[1][1], lval[1][1]+rval[1][0]))
    return lval[0] / rval[0], unit

def reduce_binop_mod(context, left, right):
    lval = reduce(context, left)
    rval = reduce(context, right)
    unit = simplity_unit((lval[1][0]+rval[1][1], lval[1][1]+rval[1][0]))
    return lval[0] % rval[0], unit

def reduce_binop_power(context, left, right):
    lval = reduce(context, left)
    rval = reduce(context, right)
    if unit_is_empty(rval[1]):
        return lval[0] ** rval[0], rval[1]
    else:
        return (None, ([], []))

def reduce_function_expr(context, params, funcname):
    return '{}({})'.format(funcname, params)

if __name__ == '__main__':
    from parser import CalcNeueParser
    calc = CalcNeueParser()
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        print(reduce({}, calc.parser.parse(s)))
