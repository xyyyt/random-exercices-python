import pytest

def replace_all_occurrences_of_the_first_char(s : str) -> str:
    return "" if not s else "".join(
        [s[0], *[s[n] if s[n] != s[0] else '$' for n in range(1, len(s))]])

@pytest.mark.parametrize("parameter, expected", [
    ("", ""),
    ("restart", "resta$t"),
    ("allllo", "allllo"),
    ("hdshahhdehhh", "hds$a$$de$$$")])
def test_replace_all_occurrences_of_the_first_char(
        parameter : str, expected : str) -> None:
    assert replace_all_occurrences_of_the_first_char(parameter) == expected
