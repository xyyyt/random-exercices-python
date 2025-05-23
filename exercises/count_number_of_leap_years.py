from calendar import isleap
from typing import Tuple
import pytest

def get_range_years(s : str) -> Tuple[int, int]:
    dash_pos : int = s.index('-')

    return int(s[0:dash_pos]), int(s[dash_pos + 1:])

def count_number_of_leap_years(s : str) -> int:
    begin_year : int
    end_year : int

    begin_year, end_year = get_range_years(s)

    counter_nb_leap_year : int = 0

    for year in range(begin_year, end_year + 1):
        if isleap(year):
            counter_nb_leap_year += 1

    return counter_nb_leap_year

@pytest.mark.parametrize("parameter, expected", [
    ("1981-1991", 2),
    ("2000-2020", 6)])
def test_count_number_of_leap_years(parameter : str, expected : int) -> None:
    assert count_number_of_leap_years(parameter) == expected
