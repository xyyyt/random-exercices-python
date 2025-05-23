from typing import Dict
import pytest

def count_occurrences_of_each_word_in_the_str(s : str) -> Dict[str, int]:
    occurrences : Dict[str, int] = {}
    n : int = 0

    while n < len(s):
        if s[n] != ' ':
            word_start_idx : int = n

            while n < len(s) and s[n] != ' ':
                n += 1

            word_end_idx : int = n
            word : str = s[word_start_idx:word_end_idx]

            if word not in occurrences:
                occurrences[word] = 1
            else:
                occurrences[word] += 1
        else:
            n += 1

    return occurrences

@pytest.mark.parametrize("parameter, expected", [
    ("", {}),
    ("abc cba", {"abc" : 1, "cba" : 1}),
    ("r abc cba abc klo klo klo   r",  {"r" : 2, "abc" : 2, "cba" : 1, "klo" : 3})])
def test_count_occurrences_of_each_word_in_the_str(
        parameter : str, expected : Dict[str, int]) -> None:
    assert count_occurrences_of_each_word_in_the_str(parameter) == expected
