def _i(i, unit=None): return 'quantity', ('integer_number', i), unit
def _f(f, unit=None): return 'quantity', ('float_number', f), unit
def input_should_match(test, fixtures):
    for input, target in fixtures.items():
        assert test(input) == target
