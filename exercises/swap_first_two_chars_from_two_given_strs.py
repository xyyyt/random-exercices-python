from typing import Tuple
import pytest

def swap_first_two_chars_from_two_given_strs(s : str, s2 : str) -> str:
    return s2[:2] + s[2:] + ' ' + s[:2] + s2[2:]

@pytest.mark.parametrize("parameter, expected", [
    (("", ""), " "),
    (("a", ""), " a"),
    (("", "b"), "b "),
    (("a", "b"), "b a"),
    (("abc", "cde"), "cdc abe")])
def test_swap_first_two_chars_from_given_strs(
        parameter : Tuple[str, str], expected : str) -> None:
    assert swap_first_two_chars_from_two_given_strs(*parameter) == expected
