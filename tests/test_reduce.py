import pytest
from functools import partial
from helpers import _i, _f, input_should_match, _sunit, _almost_equal
from calcneue.reduce import reduce

@pytest.fixture
def red():
    ctx = {
            "variables": {},
            "current_unit": None
            }
    return partial(reduce, ctx)

def test_unitless_quantity(red):
    input_should_match(red, {
         _i(1): (1, _sunit()),
         _i(0): (0, _sunit()),
         _f(4e1): (4e1, _sunit()),
    })

def test_basic_quantity(red):
    input_should_match(red, {
        _i(1, 'm'): (1, _sunit('m')),
    })


def test_reduce_convert_expr(red):
    input_should_match(red, {
        ('convert_expr', _i(1), 'm'): (1, _sunit('m')),
        ('convert_expr', _i(1, 'km'), 'm'):  (1000, _sunit('m')),
        (
            'convert_expr',
           ('binop_plus', _i(1, 'm'), _i(2)),
            'meters'
            ): (3, _sunit('m')),
        (
            'convert_expr',
            ('convert_expr', _i(1, 'm'), 'meters'),
            'm'
            ): (1, _sunit('m')),
    })

def test_basic_binop(red):
    input_should_match(red, {
        ('binop_plus', ('quantity', ('integer_number', 1), None), ('quantity', ('integer_number', 2), None)): (3, _sunit()),
        ('binop_minus', ('quantity', ('integer_number', 2), None), ('quantity', ('integer_number', 1), None)): (1, _sunit()),
        })

def test_binop_with_complex_unit(red):
    input_should_match(red,{
        # 1 m * 1 m = 1 m^2
        ('binop_multiply', ('quantity', ('integer_number', 1), 'm'), ('quantity', ('integer_number', 1), 'm')): (1, ({('m', 2)}, set())),
        # 1 m * 1 second = 1 (m * second)
        ('binop_multiply', ('quantity', ('integer_number', 1), 'm'), ('quantity', ('integer_number', 1), 'second')): (1, ({('m', 1), ('s', 1)}, set())),
        # 1 m / 1 m = 1
        ('binop_divide', ('quantity', ('integer_number', 1), 'm'), ('quantity', ('integer_number', 1), 'm')): (1, _sunit()),
        # 1 m / 1 second = 1 (m / second)
        ('binop_divide', ('quantity', ('integer_number', 1), 'm'), ('quantity', ('integer_number', 1), 'second')): (1, ({('m', 1)}, {('s', 1)})),
        })

def test_binop_power_to_quantity_with_unit(red):
    '''1 m ^ 2 foot'''
    input_should_match(red, {
    ('binop_power', ('quantity', _i(1), 'm'), ('quantity', _i(1), 'apple')): (None, _sunit()),
    })

def test_binop_power_without_unit(red):
    '''2 m ^ 2'''
    input_should_match(red, {
    ('binop_power', ('quantity', ('integer_number', 2), 'm'), ('quantity', ('integer_number', 2), None)): (4, ({('m', 2)}, set())),
    })

def test_reduce_basic_math_function(red):
    # sin(PI) should be 0
    node =  ('function_expr', ('quantity', ('float_number', 3.1415926), None), 'sin')
    assert _almost_equal(red(node)[0], 0)
    # sin(PI/2 m) should be 1 m
    node =  ('function_expr', ('quantity', ('float_number', 3.1415926/2), 'm'), 'sin')
    result = red(node)
    assert _almost_equal(result[0], 1)
    assert result[1] == _sunit('m')

def test_assignment_expr_evaluation(red):
    assert red(('assignment', ('quantity', ('integer_number', 1), 'm'), 'b')) == (1, _sunit('m'))

def test_variable_evaluation(red):
    context = { 'variables': { 'a': (1, _sunit()) }}
    assert reduce(context, ('variable', 'a', None)) == (1, _sunit())
    assert reduce(context, ('variable', 'b', None)) == (None, _sunit())

def test_assignment_side_effect(red):
    # '(a=1) + a' should be 2
    node = ('binop_plus', ('assignment', ('quantity', ('integer_number', 1), None), 'a'), ('quantity', ('integer_number', 1), None))
    assert red(node) == (2, _sunit())
    context = {"variables": {}}
    reduce(context, ('assignment', ('quantity', ('integer_number', 1), None), 'a'))
    assert context["variables"]['a'] == (1, _sunit())
    reduce(context, ('assignment', ('quantity', ('integer_number', 2), 'm'), 'a'))
    assert context["variables"]['a'] == (2, _sunit('m'))

def test_negative_expr(red):
    input_should_match(red, {
        ('negative_expr', ('quantity', ('integer_number', 1), None)): (-1, _sunit())
        })

def test_variable_add_quantity(red):
    var = ('variable', 'a', None)
    q = ('quantity', ('integer_number', 1), 'EURO')
    context = {
    'variables': {'a': (1, _sunit('EURO'))},
    }
    assert reduce(context, ('binop_plus', var, q)) == (2, _sunit('EURO'))