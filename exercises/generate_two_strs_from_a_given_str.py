from typing import Tuple, List, Dict, Set
import pytest

def generate_two_strs_from_a_given_str(s : str) -> Tuple[str, str]:
    chars_order : List[str] = []
    d : Dict[str, int] = {}

    for c in s:
        chars_order.append(c)

        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    first_str : List[str] = []
    already_used_for_first_str : Set[str] = set()
    second_str : List[str] = []
    already_used_for_second_str : Set[str] = set()

    for c in chars_order:
        if d[c] == 1 and c not in already_used_for_first_str:
            first_str.append(c)
            already_used_for_first_str.add(c)
        else:
            if c not in already_used_for_second_str:
                second_str.append(c)
                already_used_for_second_str.add(c)

    return "".join(first_str), "".join(second_str)

@pytest.mark.parametrize("parameter, expected", [
    ("", ("", "")),
    ("abbcdd", ("ac", "bd")),
    ("aebcdeffgh", ("abcdgh", "ef"))])
def test_generate_two_strs_from_a_given_str(
        parameter : str, expected : Tuple[str, str]) -> None:
    assert generate_two_strs_from_a_given_str(parameter) == expected
