import pytest

def sum_of_multiple_from_three(n : int) -> int:
    if n < 3:
        return 0

    sum_of_multiple : int = 0
    i : int = 3

    while i <= n:
        sum_of_multiple += i
        i += 2

    return sum_of_multiple

@pytest.mark.parametrize("parameter, expected", [
    (1, 0),
    (3, 3),
    (8, 15),
    (12, 35)])
def test_sum_of_multiple_from_three(parameter : int, expected : int) -> None:
    assert sum_of_multiple_from_three(parameter) == expected
