import pytest

def convert_str_to_upper_if_at_least_2_upper_chars_in_the_first_4_chars(
        s : str) -> str:
    count : int = 0

    for c in s[:4]:
        if c.isupper():
            count += 1

    return s.upper() if count >= 2 else s

@pytest.mark.parametrize("parameter, expected", [
    ("ab", "ab"),
    ("aBcd", "aBcd"),
    ("aAaAbcdf", "AAAABCDF")])
def test_convert_str_to_upper_if_at_least_2_upper_chars_in_the_first_4_chars(
        parameter : str, expected : str) -> None:
    assert convert_str_to_upper_if_at_least_2_upper_chars_in_the_first_4_chars(
        parameter) == expected
