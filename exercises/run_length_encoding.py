from typing import Optional, List
import pytest

def run_length_encoding(s : str) -> Optional[str]:
    if not s:
        return None

    rle_s : List[str] = []
    n : int = 0

    while n < len(s):
        n2 : int = n + 1

        while n2 < len(s) and s[n] == s[n2]:
            n2 += 1

        rle_s.append(str(n2 - n))
        rle_s.append(s[n])
        n = n2

    return ''.join(rle_s)

@pytest.mark.parametrize("parameter, expected", [
    ("", None),
    ("K", "1K"),
    ("aaaabbccc", "4a2b3c"),
    ("aabbaacb", "2a2b2a1c1b"),
    ("zzZzzEaaA", "2z1Z2z1E2a1A"),
    ("eBbbbBggGgiI", "1e1B3b1B2g1G1g1i1I")
])
def test_run_length_encoding(parameter : str, expected : Optional[str]) -> None:
    assert run_length_encoding(parameter) == expected
