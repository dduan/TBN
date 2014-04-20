from calcneue.reduce_unit import unit_is_empty,unit_is_equal, simplify_unit, unit_is_complex
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
    per_meter_cubed = ({}, {('m', 3)})
    per_meter_cubed_complex = ({}, {('m', 1), {'m', 2}})
    assert unit_is_equal(newton1, newton1)
    assert unit_is_equal(newton1, newton2)
    assert not unit_is_equal(m_per_ss, newton1)
    assert unit_is_equal(newton_almost, newton1)
    assert unit_is_equal(per_meter_cubed, per_meter_cubed_complex)

def test_simplify_unit():
    newton = ({('kg', 1), ('m', 1)}, {('s', 2)}) #kg*m/s^2
    newton_almost= ({('kg', 1), ('m', 1)}, {('s', 1), ('s', 1)}) #kg*m/(s*s)
    assert newton == simplify_unit(newton_almost)

def test_unit_is_complex():
    newton = ({('kg', 1), ('m', 1)}, {('s', 2)}) #kg*m/s^2
    assert not unit_is_complex(_sunit())
    assert not unit_is_complex(_sunit('m'))
    assert unit_is_complex(newton)

