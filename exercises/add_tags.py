from typing import Tuple
import pytest

def add_tags(tag : str, s : str) -> str:
    return '<' + tag + '>' + s + "</" + tag + '>'

@pytest.mark.parametrize("parameter, expected", [
    (('', ""), "<></>"),
    (('n', ""), "<n></n>"),
    (("", "Empty Tag"), "<>Empty Tag</>"),
    (('i', "Python"), "<i>Python</i>"),
    (('b', "Python Tutorial"), "<b>Python Tutorial</b>")
])
def test_add_tags(parameter : Tuple[str, str], expected : str) -> None:
    assert add_tags(*parameter) == expected
