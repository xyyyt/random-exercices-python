import pytest

def remove_repeated_consecutive_characters(s : str) -> str:
    if not s:
        return ""

    modified_str : str = ""
    n : int = 0

    while n < len(s):
        modified_str += s[n]

        if n + 1 < len(s) and s[n + 1] == s[n]:
            current_char : str = s[n]

            n += 1

            while n < len(s) and s[n] == current_char:
                n += 1
        else:
            n += 1

    return modified_str

@pytest.mark.parametrize("parameter, expected", [
    ("", ""),
    ("Red Green  Whiiiite", "Red Gren White"),
    ("aabbbcdeff66ff", "abcdef6f"),
    ("Yello42wwooddoor", "Yelo42wodor")])
def test_remove_repeated_consecutive_characters(
        parameter : str, expected : str) -> None:
     assert remove_repeated_consecutive_characters(parameter) == expected
