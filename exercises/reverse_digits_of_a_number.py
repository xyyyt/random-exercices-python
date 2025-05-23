import pytest

def reverse_digits_of_a_number(n : int) -> int:
    return int(str(n)[::-1])

@pytest.mark.parametrize("parameter, expected", [
    (0, 0),
    (42, 24),
    (364, 463),
    (12345, 54321)])
def test_reverse_digits_of_a_number(parameter : int, expected : int) -> None:
    assert reverse_digits_of_a_number(parameter) == expected
