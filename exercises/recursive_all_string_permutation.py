from typing import List
import pytest

def swap(s : List[str], idx : int, idx2 : int) -> None:
    tmp : str = s[idx]

    s[idx] = s[idx2]
    s[idx2] = tmp

def get_string_permutation(permutations : List[str], s : List[str], idx : int) -> None:
    if idx == len(s) - 1:
        permutations.append("".join(s))

        return

    for n in range(idx, len(s)):
        swap(s, idx, n)
        get_string_permutation(permutations, s, idx + 1)
        swap(s, idx, n)

def recursive_get_all_string_permutation(s) -> List[str]:
    permutations : List[str] = []

    get_string_permutation(permutations, list(s), 0)

    return permutations

@pytest.mark.parametrize("parameter, expected", [
    ("", []),
    ("ABCD", ['ABCD', 'ABDC', 'ACBD', 'ACDB', 'ADCB', 'ADBC', 'BACD',
              'BADC', 'BCAD', 'BCDA', 'BDCA', 'BDAC', 'CBAD', 'CBDA',
              'CABD', 'CADB', 'CDAB', 'CDBA', 'DBCA', 'DBAC', 'DCBA',
              'DCAB', 'DACB', 'DABC'])])
def test_recursive_get_all_string_permutation(
        parameter : str, expected : List[str]) -> None:
    assert recursive_get_all_string_permutation(parameter) == expected
