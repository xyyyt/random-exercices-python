from typing import Any, List, Tuple
import pytest

def swap(v : Any, v2 : Any) -> Tuple[Any, Any]:
    return v2, v

def shift_zero_values_at_end(l : List[int]) -> None:
    n : int = 0

    while n < len(l):
        if l[n] == 0:
            n2 : int = n + 1

            while n2 < len(l) and l[n2] == 0:
                n2 += 1

            if n2 < len(l):
                l[n], l[n2] = swap(l[n], l[n2])

        n += 1

@pytest.mark.parametrize("parameter, expected", [
    ([], []),
    ([1, 2, 0, 0], [1, 2, 0, 0]),
    ([0, 1, 0, 2, 0, 0], [1, 2, 0, 0, 0, 0]),
    ([1, 0, 0, 2, 3, 0, 4, 5], [1, 2, 3, 4, 5, 0, 0, 0])])
def test_shift_zero_values_at_end(parameter : List[int], expected : List[int]) -> None:
    shift_zero_values_at_end(parameter)

    assert parameter == expected
