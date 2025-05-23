from typing import Dict, Tuple
import pytest

def get_letters_counter(s : str) -> Dict[str, int]:
    letters_counter : Dict[str, int] = {}

    for c in s:
        c = c.lower()

        if c not in letters_counter:
            letters_counter[c] = 1
        else:
            letters_counter[c] += 1

    return letters_counter

def is_anagram(s : str, s2 : str) -> bool:
    if not s and not s2:
        return True
    elif not s or not s2:
        return False

    letters_counter_for_s : Dict[str, int] = get_letters_counter(s)
    letters_counter_for_s2 : Dict[str, int] = get_letters_counter(s2)

    return get_letters_counter(s) == get_letters_counter(s2)

@pytest.mark.parametrize("parameter, expected", [
    (("", ""), True),
    (("AbC", ""), False),
    (("", "eFg"), False),
    (("abcd", "dcba"), True),
    (("zera", "dgqs"), False),
    (("DcaAe", "aADec"), True),
    (("iniRiQue", "OniriquE"), False)])
def test_is_anagram(parameter : Tuple[str, str], expected : bool) -> None:
    assert is_anagram(*parameter) == expected
