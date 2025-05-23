from typing import List, Tuple
import pytest

def get_longest_word(words : List[str]) -> Tuple[str, int]:
    if not words:
        return "", 0

    longest_word : str = words[0]

    for word in words:
        if len(word) > len(longest_word):
            longest_word = word

    return longest_word, len(longest_word)

@pytest.mark.parametrize("parameter, expected", [
    ([], ("", 0)),
    (["ab", "bc"], ("ab", 2)),
    (["a", "ab", "abc", "abcd", "123", "dzea"], ("abcd", 4)),
    (["123456789", "", "allo", "baba", "houra"], ("123456789", 9))])
def test_get_longest_word(parameter : List[str], expected : Tuple[str, int]) -> None:
    assert get_longest_word(parameter) == expected
