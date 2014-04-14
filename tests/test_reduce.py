import pytest
from functools import partial
from helpers import _i, _f, input_should_match, _sunit
from calcneue.reduce import reduce

@pytest.fixture
def red():
    #return partial(reduce, context = {})
    return reduce

def test_unitless_quantity(red):
    input_should_match(red, {
         _i(1): (1, _sunit()),
         _i(0): (0, _sunit()),
         _f(4e1): (4e1, _sunit()),
    })

def test_basic_quantity(red):
    input_should_match(red, {
        ('quantity', _i(1), 'meter'): (1, 'meter')
    })


def test_reduce_convert_expr(red):
    input_should_match(red, {
        ( 'convert_expr', _i(1), 'meter'): (1, 'meter'),
        ('convert_expr', _i(1, 'kilometer'), 'meter'):  (1000, 'meter'),
        (
            'convert_expr',
            ('binop_plus', _i(1, 'meter'), _i(2)),
            'meters'
            ): (3, 'meter'),
        (
            'convert_expr',
            ('convert_expr', _i(1, 'meter'), 'meters'),
            'meter'
            ): (1, 'meter')
    })

def test_binop_plus(red):
    input_should_match(red, {
        ('binop_plus', ('quantity', ('integer_number', 1), None), ('quantity', ('integer_number', 2), None)): (3, None)
        })
def test_binop_power_to_quantity_with_unit(red):
    '''1 meter ^ 2 foot'''
    input_should_match(red, {
    ('binop_power', ('quantity', _i(1), 'meter'), ('quantity', _i(1), 'apple')): (None, None)
    })

