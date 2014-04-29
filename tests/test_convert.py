# -*- coding: utf-8 -*-
from calcneue.convert import convert
from helpers import _i, _f, _sunit, input_should_match

def test_unknown_units():
    assert convert((1, 'meter'), "apple") == (1, _sunit('meter'))

def test_known_units():
    assert convert((1, 'km'), 'm') == (1000, _sunit('m'))
    assert convert((318.15, "Kelvin"), "°F") == (318.15*1.8-459.67 , _sunit("°F"))
    assert convert((113, "°F"), "Kelvin") == ((113+459.67)/1.8, _sunit("Kelvin"))

def test_empty_source_unit():
    assert convert((1, None), None) == (1, _sunit())
    assert convert((1, None), 'm') == (1, _sunit('m'))


def test_a_specific_case():
    assert convert((1000, 'm'), 'km') == (1, _sunit('km'))
