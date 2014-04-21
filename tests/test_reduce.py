import pytest
from functools import partial
from helpers import _i, _f, input_should_match, _sunit, _almost_equal
from calcneue.reduce import reduce

@pytest.fixture
def red():
    return partial(reduce, {})

def test_unitless_quantity(red):
    input_should_match(red, {
         _i(1): (1, _sunit()),
         _i(0): (0, _sunit()),
         _f(4e1): (4e1, _sunit()),
    })

def test_basic_quantity(red):
    input_should_match(red, {
        _i(1, 'meter'): (1, _sunit('meter')),
    })


def test_reduce_convert_expr(red):
    input_should_match(red, {
        ('convert_expr', _i(1), 'meter'): (1, _sunit('meter')),
        ('convert_expr', _i(1, 'kilometer'), 'meter'):  (1000, _sunit('meter')),
        (
            'convert_expr',
           ('binop_plus', _i(1, 'meter'), _i(2)),
            'meters'
            ): (3, _sunit('meters')),
        (
            'convert_expr',
            ('convert_expr', _i(1, 'meter'), 'meters'),
            'meter'
            ): (1, _sunit('meter')),
    })

def test_basic_binop(red):
    input_should_match(red, {
        ('binop_plus', ('quantity', ('integer_number', 1), None), ('quantity', ('integer_number', 2), None)): (3, _sunit()),
        ('binop_minus', ('quantity', ('integer_number', 2), None), ('quantity', ('integer_number', 1), None)): (1, _sunit()),
        })

def test_binop_with_complex_unit(red):
    input_should_match(red,{
        # 1 meter * 1 meter = 1 meter^2
        ('binop_multiply', ('quantity', ('integer_number', 1), 'meter'), ('quantity', ('integer_number', 1), 'meter')): (1, ({('meter', 2)}, set())),
        # 1 meter * 1 second = 1 (meter * second)
        ('binop_multiply', ('quantity', ('integer_number', 1), 'meter'), ('quantity', ('integer_number', 1), 'second')): (1, ({('meter', 1), ('second', 1)}, set())),
        # 1 meter / 1 meter = 1
        ('binop_divide', ('quantity', ('integer_number', 1), 'meter'), ('quantity', ('integer_number', 1), 'meter')): (1, _sunit()),
        # 1 meter / 1 second = 1 (meter / second)
        ('binop_divide', ('quantity', ('integer_number', 1), 'meter'), ('quantity', ('integer_number', 1), 'second')): (1, ({('meter', 1)}, {('second', 1)})),
        })

def test_binop_power_to_quantity_with_unit(red):
    '''1 meter ^ 2 foot'''
    input_should_match(red, {
    ('binop_power', ('quantity', _i(1), 'meter'), ('quantity', _i(1), 'apple')): (None, _sunit()),
    })

def test_reduce_basic_math_function(red):
    # sin(PI) should be 0
    node =  ('function_expr', ('quantity', ('float_number', 3.1415926), None), 'sin')
    assert _almost_equal(red(node)[0], 0)
    # sin(PI/2 meter) should be 1 meter
    node =  ('function_expr', ('quantity', ('float_number', 3.1415926/2), 'meter'), 'sin')
    result = red(node)
    assert _almost_equal(result[0], 1)
    assert result[1] == _sunit('meter')

def test_assignment_expr_evaluation(red):
    assert red(('assignment', ('quantity', ('integer_number', 1), 'meter'), 'b')) == (1, _sunit('meter'))

def test_varialbe_evaluation(red):
    context = { 'a': (1, _sunit()) }
    assert reduce(context, ('variable', 'a', None)) == (1, _sunit())
    assert reduce(context, ('variable', 'b', None)) == (None, _sunit())

def test_assignment_side_effect(red):
    # '(a=1) + a' should be 2
    node = ('binop_plus', ('assignment', ('quantity', ('integer_number', 1), None), 'a'), ('quantity', ('integer_number', 1), None))
    assert red(node) == (2, _sunit())
