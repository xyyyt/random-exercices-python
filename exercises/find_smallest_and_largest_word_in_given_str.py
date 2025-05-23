from typing import Tuple
import pytest

def find_smallest_and_largest_word_in_given_str(s : str) -> Tuple[str, str]:
    if not s:
        return "", ""

    smallest_word : str = ""
    largest_word : str = ""

    for word in s.split():
        if smallest_word == "":
            smallest_word = word
        elif len(word) < len(smallest_word):
            smallest_word = word

        if largest_word == "":
            largest_word = word
        elif len(word) > len(largest_word):
            largest_word = word

    return smallest_word, largest_word

@pytest.mark.parametrize("parameter, expected", [
    ("", ("", "")),
    ("abcd", ("abcd", "abcd")),
    ("  abc  efg   hij ", ("abc", "abc")),
    ("  abcd e fgh ijklm nop", ("e", "ijklm"))])
def test_find_smallest_and_largest_word_in_given_str(
        parameter : str, expected : Tuple[str, str]) -> None:
    assert find_smallest_and_largest_word_in_given_str(parameter) == expected
