from typing import List
import pytest

def get_permuted_str_on_each_two_index(s : str) -> str:
    if not s:
        return ""

    permuted_s : List[str] = list(s)

    for n in range(0, len(s) - 1, 2):
        a : str = permuted_s[n + 1]
        b : str = permuted_s[n]

        permuted_s[n] = a
        permuted_s[n + 1] = b

    return "".join(permuted_s)

@pytest.mark.parametrize("parameter, expected", [("", ""), ("ABCDE", "BADCE")])
def test_get_permuted_str_on_each_two_index(parameter : str, expected : str) -> None:
    assert get_permuted_str_on_each_two_index(parameter) == expected
