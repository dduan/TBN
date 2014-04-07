from __future__ import print_function, unicode_literals, division
from convert import convert, lookup_base_unit
def reduce(node):
    print('reducing {}'.format(node))
    return globals()['reduce_' + node[0]](*node[1:])

def reduce_quantity(number, unit):
	baseunit = lookup_base_unit(unit)
	return convert((number, unit), baseunit)

def reduce_float_number(s):
    return float(s)

def reduce_integer_number(s):
    return int(s)

def reduce_convert_expr(expr, unit):
    #TODO: actually convert it
    return convert(reduce(expr), unit)

def reduce_assignment(expr, id):
    #TODO: implement side effects aka register id
    return reduce(expr)

def reduce_group_expr(expr):
    return reduce(expr)

def reduce_binop_plus(left, right):
    lval = reduce(left)
    rval = reduce(right)
    return lval[0] + rval[0], rval[1]

def reduce_binop_minus(left, right):
    lval = reduce(left)
    rval = reduce(right)
    return lval[0] - rval[0], rval[1]

def reduce_binop_multiply(left, right):
    lval = reduce(left)
    rval = reduce(right)
    return lval[0] * rval[0], rval[1]

def reduce_binop_divide(left, right):
    lval = reduce(left)
    rval = reduce(right)
    return lval[0] / rval[0], rval[1]

def reduce_binop_mod(left, right):
    lval = reduce(left)
    rval = reduce(right)
    return lval[0] % rval[0], rval[1]

def reduce_binop_power(left, right):
    lval = reduce(left)
    rval = reduce(right)
    return lval[0] ** rval[0], rval[1]

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
