from calcneue.convert import convert
from helpers import _i, _f, _sunit, input_should_match

def test_unknown_units():
    assert convert((1, 'meter'), "apple") == (1, _sunit('meter'))

def test_known_units():
    assert convert((1, 'kilometer'), 'meter') == (1000, _sunit('meter'))
    assert convert((45, "celsius"), "farenheit") == (113, _sunit("farenheit"))
    assert convert((113, "farenheit"), "celsius") == (45, _sunit("celsius"))

def test_empty_source_unit():
    assert convert((1, None), None) == (1, _sunit())
