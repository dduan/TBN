from calcneue.convert import convert
from calcneue.helpers import _i, _f, input_should_match

def test_unknown_units():
	assert convert(_i(1, "meter"), "apple") == (1, "meter")
