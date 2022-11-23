import pytest

from ttt.board import hi

hi_inp_out = [
    ("Suresh", "Hi Suresh!"),
    ("Mohit", "Hi Mohit!"),
    ("Ramesh", "Hi Ramesh!"),
]


@pytest.mark.parametrize("input, output", hi_inp_out)
def test_hi(input, output):
    assert hi(input) == output
