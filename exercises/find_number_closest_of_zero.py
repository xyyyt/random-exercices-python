from typing import List, Optional
import pytest

def find_number_closest_of_zero(l : List[int]) -> Optional[int]:
    if not l:
        return None

    number_closest_of_zero : int = l[0]
    n : int = 1

    while n < len(l):
        if abs(l[n]) < abs(number_closest_of_zero):
            number_closest_of_zero = l[n]

        n += 1

    return number_closest_of_zero

@pytest.mark.parametrize("parameter, expected", [
    ([], None),
    ([1, 4], 1),
    ([-2, -6, -12, 4], -2),
    ([-3, 5, 1, 9, -42, -1], 1)])
def test_find_number_closest_of_zero(parameter : List[int], expected : Optional[int]) -> None:
    assert find_number_closest_of_zero(parameter) == expected
