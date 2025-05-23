from typing import Tuple
import pytest

def remove_nth_index_of_the_str(s : str, idx : int) -> str:
    if not s:
        return ""
    elif idx < 0:
        return s
    else:
        return s[0:idx] + s[idx + 1:]

@pytest.mark.parametrize("parameter, expected", [
    (("", 0), ""),
    (("ab", -1), "ab"),
    (("abc", 0), "bc"),
    (("abcd", 1), "acd"),
    (("abcde", 4), "abcd"),
    (("abcdef", 42), "abcdef")])
def test_remove_nth_index_of_the_str(
        parameter : Tuple[str, int], expected : str) -> None:
    assert remove_nth_index_of_the_str(*parameter) == expected
