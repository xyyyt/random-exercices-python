from typing import List, Any
import pytest

def recursive_build_reversed_array(a : List[Any]) -> List[Any]:
    if not a:
        return []

    def fill_reversed_array(a : List[Any], n : int, a2 : List[Any]) -> None:
        if n >= len(a):
            return

        fill_reversed_array(a, n + 1, a2)
        a2.append(a[n])

    a2 : List[Any] = []

    fill_reversed_array(a, 0, a2)

    return a2

@pytest.mark.parametrize("parameter, expected", [
    ([0, 1, 2, 3, 4], [4, 3, 2, 1, 0]),
    (['a', 'b', 'c', 'd', 'e'], ['e', 'd', 'c', 'b', 'a']),
    (["abcd", "efgh", "ijkl", "mnlo", "pqrs"], ["pqrs", "mnlo", "ijkl", "efgh", "abcd"])])
def test_recursive_build_reversed_array(parameter : List[Any], expected : List[Any]) -> None:
    assert recursive_build_reversed_array(parameter) == expected
