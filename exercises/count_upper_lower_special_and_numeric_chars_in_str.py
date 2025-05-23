from typing import Tuple
import pytest

def count_upper_lower_special_and_numeric_chars_in_str(s : str) -> \
    Tuple[int, int, int, int]:
    upper_count : int = 0
    lower_count : int = 0
    special_count : int = 0
    numeric_count : int = 0

    for c in s:
        ascii_code = ord(c)

        if ascii_code >= 65 and ascii_code <= 90:
            upper_count += 1
        elif ascii_code >= 97 and ascii_code <= 122:
            lower_count += 1
        elif (ascii_code >= 32 and ascii_code <= 47) \
             or (ascii_code >= 58 and ascii_code <= 64) \
             or (ascii_code >= 91 and ascii_code <= 96) \
             or (ascii_code >= 123 and ascii_code <= 126):
            special_count += 1
        elif ascii_code >= 48 and ascii_code <= 57:
            numeric_count += 1

    return upper_count, lower_count, special_count, numeric_count

@pytest.mark.parametrize("parameter, expected", [
    ("", (0, 0, 0, 0)),
    ("12345==()", (0, 0, 4, 5)),
    ("aBCDeFgH", (5, 3, 0, 0)),
    ("1b3c?*[d9)=4", (0, 3, 5, 4))])
def test_count_upper_lower_special_and_numeric_chars_in_str(
        parameter : str, expected : Tuple[int, int, int, int]) -> None:
    assert count_upper_lower_special_and_numeric_chars_in_str(parameter) == expected
