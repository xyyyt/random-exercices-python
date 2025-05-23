from typing import Optional
import pytest

def compute_check_code(s : str) -> Optional[int]:
    if not s or not s.isnumeric():
        return None

    sum_of_numbers_on_even_indexes : int = 0
    sum_of_numbers_on_odd_indexes : int = 0
    n : int = 0

    while n < len(s):
        if n % 2 == 0:
            sum_of_numbers_on_even_indexes += int(s[n])
        else:
            sum_of_numbers_on_odd_indexes += int(s[n])

        n += 1

    check_code : int = sum_of_numbers_on_even_indexes * 3 + sum_of_numbers_on_odd_indexes

    return check_code if check_code % 10 == 0 else check_code - 7

@pytest.mark.parametrize("parameter, expected", [
    ("", None),
    ("1234abcd5678", None),
    ("5", 8),
    ("3124", 20),
    ("240", 10)])
def test_compute_check_code(parameter : str, expected : Optional[int]) -> None:
    assert compute_check_code(parameter) == expected
