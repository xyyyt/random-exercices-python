from typing import Set, Tuple, Dict
import copy
import pytest

def find_windows_in_str(s : str, s2 : str) -> Set[str]:
    if not s or not s2:
        return set()

    d : Dict[str, int] = {}

    for c in s2:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1

    windows : Set[str] = set()
    n : int = 0

    while n < len(s):
        if s[n] in s2:
            old_n : int = n
            d2 : Dict[str, int] = copy.deepcopy(d)
            n2 : int = 0

            while n < len(s) and n2 < len(s2) and d2:
                if s[n] in d2:
                    if d2[s[n]] == 1:
                        del d2[s[n]]
                    else:
                        d2[s[n]] -= 1

                    n2 += 1

                n += 1

            if not d2:
                windows.add(s[old_n:n])

        else:
            n += 1

    return windows

@pytest.mark.parametrize("parameter, expected", [
    (("", ""), set()),
    (("abcd", ""), set()),
    (("", "abcd"), set()),
    (("PRWOERIUSFK", "OSU"), {"OERIUS"}),
    (("abghcd12345abghcd", "dcab"), {"abghcd"}),
    (("abcd12HJJgtJabHvf2pa1JJ", "J21JH"), {"12HJJ", "JabHvf2pa1J"})])
def test_find_windows_in_str(parameter : Tuple[str, str], expected : Set[str]) -> None:
    assert find_windows_in_str(*parameter) == expected
