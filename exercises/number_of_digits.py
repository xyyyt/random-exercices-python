import pytest

def number_of_digits(n : int) -> int:
    digits_nb : int = 0
    denominator : int = 1

    while True:
        digits_nb += 1
        denominator *= 10

        if n // denominator == 0:
            break

    return digits_nb

@pytest.mark.parametrize("parameter, expected", [
    (0, 1),
    (4, 1),
    (12, 2),
    (40, 2),
    (742, 3),
    (9542, 4)])
def test_number_of_digits(parameter : int, expected : int) -> None:
    assert number_of_digits(parameter) == expected
