from codeschool.questions.coding_io.utils import expand_from_code
from iospec import IoSpec, Out, In, SimpleTestCase


def test_expand_from_code_keep_simple_cases():
    src = "print(input('x:'))"
    iospec = (
        'x: <foo>\n'
        'foo\n'
        '\n'
        '@input $name\n'
        '\n'
        'x: <bar>\n'
        'bar'
    )
    iospec = IoSpec(iospec)
    expanded = expand_from_code(src, iospec, lang='python')
    expected = SimpleTestCase([Out('x: '), In('foo'), Out('foo')])
    assert expanded[0] == expected