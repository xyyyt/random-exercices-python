import pytest

def shortened_str_from_chars_first_and_last_two(s : str) -> str:
    return "" if len(s) < 2 else s[0:2] + s[-2:]

@pytest.mark.parametrize("parameter, expected", [
    ("w3resource", "w3ce"),
    ("w3", "w3w3"),
    ("w", "")])
def test_shortened_str_from_chars_first_and_last_two(
        parameter : str, expected : str) -> None:
    assert shortened_str_from_chars_first_and_last_two(parameter) == expected
