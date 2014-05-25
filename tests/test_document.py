'''
End-to-end black-box testing.
These should also serve as documentation for overall functionality
'''

from calcneue.document import Document

TEST_DATA = {
    '1 + 1': ['2'],
}

def test_data():
    for input, output in TEST_DATA.items():
        doc = Document(input)
        assert( output == doc.evaluate() )
