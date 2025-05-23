import pytest

def swap_first_and_last_char_of_the_str(s : str) -> str:
    return s if len(s) < 2 else s[len(s) - 1] + s[1:len(s) - 1] + s[0]

@pytest.mark.parametrize("parameter, expected", [
    ("", ""),
    ("a", "a"),
    ("ab", "ba"),
    ("abc", "cba")])
def test_swap_first_and_last_char_of_the_str(parameter : str, expected : str) -> None:
    assert swap_first_and_last_char_of_the_str(parameter) == expected
