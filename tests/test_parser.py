import pytest
from calcneue.parser import CalcNeueParser
from helpers import _i, _f, input_should_match

@pytest.fixture
def calc(): return CalcNeueParser().parser.parse

def test_number_only_quantity(calc):
    input_should_match(calc, {
        '42': _i(42),
        '0o3': _i(3),
        '0': _i(0),
        '3e2': _f(3e2),
        '0.3': _f(0.3),
    })

def test_unit_quantity(calc):
    input_should_match(calc, {
        '2 inch': _i(2, 'inch'),
        '3e7 km': _f(3e7, 'km'),
        '0 kblam': _i(0, 'kblam'),
    })

def test_unit_variable(calc):
    input_should_match(calc, {
        'a inch': ('variable', 'a', 'inch'),
        'cos(a meter)': ('function_expr', ('variable', 'a', 'meter'), 'cos'),
    })

def test_function_expr(calc):
    input_should_match(calc, {
        'sin(0.4)': ('function_expr', _f(0.4), 'sin'),
        'blow(0.4)': ('function_expr', _f(0.4), 'blow'),
        'wat(1+2)': (
            'function_expr',
            ('binop_plus', _i(1), _i(2),),
            'wat'
        ),
    })

def test_convert_expr(calc):
    input_should_match(calc, {
        '1 in meters': ( 'convert_expr', _i(1), 'meters'),
        '1 inch in meters':('convert_expr', _i(1, 'inch'), 'meters'),
        '1 inch + 2 in meters': (
            'convert_expr',
            ('binop_plus', _i(1, 'inch'), _i(2)),
            'meters'
        ),
        '1 inch in meters in lightyears': (
            'convert_expr',
            ('convert_expr', _i(1, 'inch'), 'meters'),
            'lightyears'
        ),
    })

def test_group_expr(calc):
    input_should_match(calc, {
        '1 + ( 2 + 3 )': ('binop_plus', _i(1), ('binop_plus', _i(2), _i(3))),
        '1 / ( 2 + 3 )': ('binop_divide', _i(1), ('binop_plus', _i(2), _i(3))),
        '( 2 + 3 ) / 1': ('binop_divide', ('binop_plus', _i(2), _i(3)), _i(1)),
    })

def test_binop_power(calc):
    input_should_match(calc, {
        '2 ^ 2': ('binop_power', _i(2), _i(2)),
        '1 + 2 ^ 2': ('binop_plus', _i(1), ('binop_power', _i(2), _i(2))),
        '1 / 2 ^ 2': ('binop_divide', _i(1), ('binop_power', _i(2), _i(2))),
        '1 ^ 2 ^ 2': ('binop_power', _i(1), ('binop_power', _i(2), _i(2))),
    })

def test_binop_mod(calc):
    input_should_match(calc, {
        '2 % 2': ('binop_mod', _i(2), _i(2)),
        '1 + 2 % 2': ('binop_plus', _i(1), ('binop_mod', _i(2), _i(2))),
        '1 / 2 % 2': ('binop_mod', ('binop_divide', _i(1), _i(2)), _i(2)),
        '1 % 2 ^ 2': ('binop_mod', _i(1), ('binop_power', _i(2), _i(2))),
    })

def test_binop_divide(calc):
    input_should_match(calc, {
        '2 / 2': ('binop_divide', _i(2), _i(2)),
        '1 + 2 / 2': ('binop_plus', _i(1), ('binop_divide', _i(2), _i(2))),
        '1 / 2 / 2': ('binop_divide', ('binop_divide', _i(1), _i(2)), _i(2)),
        '1 / 2 ^ 2': ('binop_divide', _i(1), ('binop_power', _i(2), _i(2))),
    })

def test_binop_multiply(calc):
    input_should_match(calc, {
        '2 * 2': ('binop_multiply', _i(2), _i(2)),
        '1 + 2 * 2': ('binop_plus', _i(1), ('binop_multiply', _i(2), _i(2))),
        '1 / 2 * 2': ('binop_multiply', ('binop_divide', _i(1), _i(2)), _i(2)),
        '1 * 2 ^ 2': ('binop_multiply', _i(1), ('binop_power', _i(2), _i(2))),
    })

def test_binop_minus(calc):
    input_should_match(calc, {
        '2 - 2': ('binop_minus', _i(2), _i(2)),
        '1 + 2 - 2': ('binop_minus', ('binop_plus', _i(1), _i(2)), _i(2)),
        '1 - 2 * 2': ('binop_minus', _i(1) ,('binop_multiply', _i(2), _i(2))),
        '1 - 2 ^ 2': ('binop_minus', _i(1), ('binop_power', _i(2), _i(2))),
    })

def test_binop_plus(calc):
    input_should_match(calc, {
        '2 + 2': ('binop_plus', _i(2), _i(2)),
        '1 + 2 + 2': ('binop_plus', ('binop_plus', _i(1), _i(2)), _i(2)),
        '1 + 2 * 2': ('binop_plus', _i(1) ,('binop_multiply', _i(2), _i(2))),
        '1 + 2 ^ 2': ('binop_plus', _i(1), ('binop_power', _i(2), _i(2))),
    })

def test_assignment(calc):
    input_should_match(calc, {
        'a = 1': ('assignment', _i(1), 'a'),
        'a = 1 ^ 2': ('assignment', ('binop_power', _i(1), _i(2)), 'a'),
        '42 % a = 1': ('binop_mod', _i(42), ('assignment', _i(1), 'a')),
        'cos(a = 1)': ('function_expr', ('assignment', _i(1), 'a'), 'cos'),
    })

def test_negative_expr(calc):
    input_should_match(calc, {
        '-1': ('negative_expr', _i(1)),
        '-sin(2)': ('negative_expr', ('function_expr', _i(2), 'sin')),
        '-(2 % 3)': ('negative_expr', ('binop_mod', _i(2), _i(3))),
        '2 + -3': ('binop_plus', _i(2), ('negative_expr', _i(3))),
        '2 / -3': ('binop_divide', _i(2), ('negative_expr', _i(3))),
        '2 ^ -3': ('binop_power', _i(2), ('negative_expr', _i(3))),
    })

