from __future__ import print_function, unicode_literals, division
from calcneue.convert import convert, lookup_base_unit
from calcneue.reduce_unit import *

# TODO:
# variables
# use unknown units
# tolerate partial errors 
context = {}
def reduce(node):
    print('reducing {}'.format(node))
    return globals()['reduce_' + node[0]](*node[1:])

def reduce_quantity(number, unit):
    baseunit = lookup_base_unit(unit)
    #print(number)
    print("calling convert from reduce_quantity")
    return convert((number[1], unit), baseunit)

def reduce_float_number(s):
    return float(s)

def reduce_integer_number(s):
    return int(s)

def reduce_convert_expr(expr, unit):
    expr = reduce(expr)
    if unit_is_complex(expr[1]):
        return reduce(expr)
    else:
        print("calling convert from reduce_convert_quantity")
        return convert((expr[0], expr[1][0][0]), unit)

def reduce_assignment(expr, id):
    #TODO: implement side effects aka register id
    return reduce(expr)

def reduce_binop_plus(left, right):
    lval = reduce(left)
    rval = reduce(right)
    if (unit_is_equal(lval[1], rval[1])):
        return lval[0] + rval[0], rval[1]
    elif (unit_is_empty(lval[1])):
        return lval[0] + rval[0], rval[1]
    elif (unit_is_empty(rval[1])):
        return lval[0] + rval[0], lval[1]
    else:
        return (None, ([], []))

def reduce_binop_minus(left, right):
    lval = reduce(left)
    rval = reduce(right)
    if (unit_is_equal(lval[1], rval[1])):
        return lval[0] - rval[0], rval[1]
    elif (unit_is_empty(lval[1])):
        return lval[0] - rval[0], rval[1]
    elif (unit_is_empty(rval[1])):
        return lval[0] - rval[0], lval[1]
    else:
        return (None, ([], []))

def reduce_binop_multiply(left, right):
    lval = reduce(left)
    rval = reduce(right)
    unit = simplity_unit((lval[1][0]+rval[1][0], lval[1][1]+rval[1][1]))
    return lval[0] * rval[0], unit

def reduce_binop_divide(left, right):
    lval = reduce(left)
    rval = reduce(right)
    unit = simplity_unit((lval[1][0]+rval[1][1], lval[1][1]+rval[1][0]))
    return lval[0] / rval[0], unit

def reduce_binop_mod(left, right):
    lval = reduce(left)
    rval = reduce(right)
    unit = simplity_unit((lval[1][0]+rval[1][1], lval[1][1]+rval[1][0]))
    return lval[0] % rval[0], unit

def reduce_binop_power(left, right):
    lval = reduce(left)
    rval = reduce(right)
    if unit_is_empty(rval[1]):
        return lval[0] ** rval[0], rval[1]
    else:
        return (None, ([], []))

def reduce_function_expr(params, funcname):
    return '{}({})'.format(funcname, params)

if __name__ == '__main__':
    from parser import CalcNeueParser
    calc = CalcNeueParser()
    while True:
        try:
            s = input('calc > ')
        except EOFError:
            break
        print(reduce(calc.parser.parse(s)))
