import pytest

def add_ing_on_end_of_the_str(s : str) -> str:
    return s if len(s) < 3 else s[0:len(s) - 3] + ("ing" if s[-3:] != "ing" else "ly")

@pytest.mark.parametrize("parameter, expected", [
    ("", ""),
    ("a", "a"),
    ("ab", "ab"),
    ("abc", "ing"),
    ("ing", "ly"),
    ("inging", "ingly"),
    ("abcly", "abing")])
def test_add_ing_on_end_of_the_str(parameter : str, expected : str) -> None:
    assert add_ing_on_end_of_the_str(parameter) == expected
