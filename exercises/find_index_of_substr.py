from typing import Tuple
import pytest

def find_index_of_substr(s : str, s2 : str) -> int:
    if not s or not s2:
        return -1

    n : int = 0

    while n < len(s):
        if s[n] == s2[0]:
            n2 : int = n
            n3 : int = 0

            while n2 < len(s) and n3 < len(s2) and s[n2] == s2[n3]:
                n2 += 1
                n3 += 1

            if n3 == len(s2):
                break

        n += 1

    return n

@pytest.mark.parametrize("parameter, expected", [
    (("", ""), -1),
    (("abcd", ""), -1),
    (("abcdefg", "cde"), 2),
    (("abcccdefg", "cd"), 4),
    (("ab123123cd", "123"), 2)])
def test_find_index_of_substr(parameter : Tuple[str, str], expected : int) -> None:
    assert find_index_of_substr(*parameter) == expected
