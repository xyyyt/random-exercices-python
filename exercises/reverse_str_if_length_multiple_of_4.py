import pytest

def reverse_str_if_length_multiple_of_4(s : str) -> str:
    return s[::-1] if len(s) % 4 == 0 else s

@pytest.mark.parametrize("parameter, expected", [
    ("", ""),
    ("a", "a"),
    ("ab", "ab"),
    ("abc", "abc"),
    ("abcd", "dcba"),
    ("abcdefgh", "hgfedcba")])
def test_reverse_str_if_length_multiple_of_4(parameter : str, expected : str) -> None:
    assert reverse_str_if_length_multiple_of_4(parameter) == expected
