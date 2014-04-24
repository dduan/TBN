from calcneue.reduce_unit import *
from helpers import _sunit

def test_unit_is_empty():
    assert unit_is_empty(_sunit())
    assert not unit_is_empty(({('meter', 1)}, set()))

def test_unit_is_equal_simple_cases():
    assert unit_is_equal(_sunit(), _sunit())
    assert unit_is_equal(_sunit('meter'), _sunit('meter'))
    assert not unit_is_equal(_sunit(), _sunit('meter'))
    assert not unit_is_equal(_sunit('meter'), _sunit())
    assert not unit_is_equal(_sunit('meter'), _sunit('kg'))

def test_unit_is_equal_complex_cases():
    m_per_ss = ({('meter', 1)}, {('s', 2)})
    newton1 = ({('kg', 1), ('m', 1)}, {('s', 2)}) #kg*m/s^2
    newton2 = ({('kg', 1), ('m', 1)}, {('s', 2)}) #kg*m/s^2
    per_meter_cubed = (set(), {('m', 3)})
    per_meter_cubed_complex = (set(), {('m', 1), ('m', 2)})
    assert unit_is_equal(newton1, newton1)
    assert unit_is_equal(newton1, newton2)
    assert not unit_is_equal(m_per_ss, newton1)
    assert unit_is_equal(per_meter_cubed, per_meter_cubed_complex)

def test_simplify_unit():
    per_meter_cubed = (set(), {('m', 3)})
    per_meter_cubed_complex = (set(), {('m', 1), ('m', 2)})
    assert per_meter_cubed == simplify_unit(per_meter_cubed_complex)

def test_unit_is_complex():
    newton = ({('kg', 1), ('m', 1)}, {('s', 2)}) #kg*m/s^2
    assert not unit_is_complex(_sunit())
    assert not unit_is_complex(_sunit('m'))
    assert unit_is_complex(newton)

def test_unit_multiply_simple():
    assert unit_multiply(_sunit('m'), _sunit('m')) == ({('m', 2)}, set())
    assert unit_multiply(_sunit('m'), _sunit()) == _sunit('m')
    assert unit_multiply(_sunit(), _sunit('m')) == _sunit('m')

def test_unit_multiply_complex():
    a = ({('m', 1), ('kg', 1)}, set())
    b = (set(), {('s', 2)})
    newton = ({('kg', 1), ('m', 1)}, {('s', 2)}) #kg*m/s^2
    assert unit_multiply(a, b) == newton

def test_unit_divide_simple():
    assert unit_divide(_sunit('m'), _sunit('m')) == _sunit()
    assert unit_divide(_sunit('m'), _sunit()) == _sunit('m')
    assert unit_divide(_sunit(), _sunit('m')) == (set(), {('m', 1)})

def test_unit_divide_complex():
    a = ({('m', 1), ('kg', 1)}, set())
    b = ({('s', 2)}, set())
    newton = ({('kg', 1), ('m', 1)}, {('s', 2)}) #kg*m/s^2
    assert unit_divide(a, b) == newton

def test_unit_power():
    m_per_ss = ({('m', 1)}, {('s', 2)})
    mm_per_ssss = ({('m', 2)}, {('s', 4)})
    assert unit_power(m_per_ss, 2) == mm_per_ssss
