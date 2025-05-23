import pytest

def remove_odd_index_of_the_str(s : str) -> str:
    return "".join([s[n] for n in range(0, len(s), 2)])

@pytest.mark.parametrize("parameter, expected", [
    ("", ""),
    ("a", "a"),
    ("ab", "a"),
    ("abc", "ac"),
    ("abcd", "ac"),
    ("abcde", "ace")])
def test_remove_odd_index_of_the_str(parameter : str, expected : str) -> None:
    assert remove_odd_index_of_the_str(parameter) == expected
