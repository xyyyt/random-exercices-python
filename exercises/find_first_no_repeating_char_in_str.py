from typing import List, Dict
import pytest

def find_first_no_repeating_char_in_str(s : str) -> str:
    if not s:
        return ""

    chars_order : List[str] = []
    d : Dict[str, int] = {}

    for c in s:
        chars_order.append(c)

        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    for c in chars_order:
        if d[c] == 1:
            return c

    return ""

@pytest.mark.parametrize("parameter, expected", (("", ""), ("abbcd", "a"), ("acdca", "d")))
def test_find_first_no_repeating_char_in_str(parameter : str, expected : str) -> None:
    assert find_first_no_repeating_char_in_str(parameter) == expected
