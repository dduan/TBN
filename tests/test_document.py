'''
End-to-end black-box testing.
These should also serve as documentation for overall functionality
'''

from calcneue.document import Document
from helpers import _almost_equal

def test_integers():
    TEST_DATA = {
        '42': ['42'],
        '0': ['0'],
        ' 1 ' : ['1'],
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def test_negative_exp():
    TEST_DATA = {
        '-2' : '-2',
        '--3' : '3',
        '- 5' : '-5',
        '-0' : '0',
        ' - 4 ' : '-4',
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def test_addition():
    TEST_DATA = {
        '1 + 1': ['2'],
        '1 + ( 2 + 3 )': ['6'],
        '2 + 2': ['4'],
        '0 + 5' : ['5'],
        '-1 + 5' : ['4'],
        '5 + -1' : ['4'],
        '-1 + -7' : ['-8'],
        '5 + -2 + 9' : ['12'],
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def subtraction():
    TEST_DATA = {
        '1 - 1': ['0'],
        '1 - ( 2 - 3 )': ['2'],
        '2 - 2': ['0'],
        '0 - 5' : ['-5'],
        '-1 - 5' : ['-6'],
        '5 - -1' : ['6'],
        '-1 - -7' : ['6'],
        '5 - -2 - 9' : ['-2'],
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def test_multiplication():
    TEST_DATA = {
        '1 * 1': ['1'],
        '1 * ( 2 * 3 )': ['6'],
        '2 * 2': ['4'],
        '0 * 5' : ['0'],
        '-1 * 5' : ['-5'],
        '5 * -1' : ['-5'],
        '-1 * -7' : ['7'],
        '5 * -2 * 9' : ['-90'],
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def test_division():
    TEST_DATA = {
        '1 / 1': ['1'],
        '1 / ( 2 / 3 )': ['1.5'],
        '2 / 2': ['1'],
        '0 / 5' : ['0'],
        '5 / 0' : [''],
        '-1 / 5' : ['-0.2'],
        '5 / -1' : ['-5'],
        '-1 / -7' : ['-0.14285714285'],
        '5 / -2 / 9' : ['-0.27777777777'],
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( _almost_equal(output, doc.evaluate() ) )


def test_powers():
    TEST_DATA = {
        '1 ^ 1': ['1'],
        '1 ^ ( 2 ^ 3 )': ['1'],
        '2 ^ 2': ['4'],
        '0 ^ 5' : ['0'],
        '5 ^ 0' : ['1'],
        '-1 ^ 5' : ['-1'],
        '5 ^ -1' : ['0.2'],
        '-1 ^ -7' : ['-1'],
        '4 ^ -2 ^ 3' : ['0.00001525878'],
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( _almost_equal(output, doc.evaluate() ) )


def test_mod():
    TEST_DATA = {
        '1 % 1': ['0'],
        '1 % ( 2 % 3 )': ['1'],
        '2 % 2': ['0'],
        '0 % 5' : ['0'],
        '5 % 0' : ['0'],
        '-1 % 5' : ['4'],
        '5 % -1' : [0.2''],
        '-1 % -7' : ['-1'],
        '4 % -2 % 3' : ['0'],
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def test_combined_functions():
    TEST_DATA = {
        '1 / ( 2 + 3 )': ['0.2'],
        '( 2 + 3 ) / 1': ['5'],
        '1 + 2 ^ 2': ['5'],
        '1 / 2 ^ 2': ['0.25'],
        '1 ^ 2 ^ 2': ['1'],
        '1 + 2 % 2': ['1'],
        '1 / 2 % 2': [''],
        '1 % 2 ^ 2': ['1'],
        '1 + 2 / 2': ['2'],
        '1 / 2 / 2': ['0.25'],
        '1 / 2 ^ 2': ['0.25'],
        '1 + 2 * 2': ['5'],
        '1 / 2 * 2': ['1'],
        '1 * 2 ^ 2': ['4'],
        '1 + 2 - 2': ['0'],
        '1 - 2 * 2': ['-3'],
        '1 - 2 ^ 2': ['-3'],
        '1 + 2 + 2': ['5'],
        '1 + 2 * 2': ['5'],
        '1 + 2 ^ 2': ['5'],
        '1 + 2 + 2': ['5'],
        '1 + 2 * 2': ['5'],
        '1 + 2 ^ 2': ['5'],
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def test_math_functions():
    TEST_DATA = {
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( _almost_equal(output, doc.evaluate() ) )


def test_sci_notation():
    TEST_DATA = {
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def test_explicit_convert():
    TEST_DATA = {    
        '1 m in km': ['.001 km'],
        '1 m + 2 in meters' : ['3 meters'],
        '1 m in meters in m' : ['1 m'],
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def test_assignment():
    TEST_DATA = {    
        'a = 1': ['1'],
        'a = 1 ^ 2': ['1'],
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def test_use_variables():
    TEST_DATA = {
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def test_simple_units():
    TEST_DATA = {
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def test_add_units():
    TEST_DATA = {
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def test_sub_units():
    TEST_DATA = {
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def test_mult_units():
    TEST_DATA = {
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )


def test_div_units():
    TEST_DATA = {
    }
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )
