from typing import Dict
import pytest

def count_nb_of_chars_in_str(s : str) -> Dict[str, int]:
    d : Dict[str, int] = {}

    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    return d

@pytest.mark.parametrize("parameter, expected", [
    ("", {}),
    ("aabc", {'a' : 2, 'b' : 1, 'c' : 1}),
    ("12345244", {'1' : 1, '2' : 2, '3' : 1, '4' : 3, '5' : 1}),
    ("youha", {'y' : 1, 'o' : 1, 'u' : 1, 'h' : 1, 'a' : 1}),
    ("hhahh", {'h' : 4, 'a' : 1})])
def test_count_nb_of_chars_in_str(parameter : str, expected : Dict[str, int]) -> None:
    assert count_nb_of_chars_in_str(parameter) == expected
