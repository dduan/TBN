import pytest
from functools import partial
from helpers import _i, _f, input_should_match
from calcneue.reduce import reduce

@pytest.fixture
def red():
    return partial(reduce, context = {})

def test_unitless_quantity(red):
    input_should_match(red, {
        _i(1): (1, None),
        _i(0): (0, None),
        _i(2e1): (2e1, None),
    })
