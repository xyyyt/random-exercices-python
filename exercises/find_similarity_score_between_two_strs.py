from typing import Tuple
import pytest

def find_similarity_score_between_two_strs(s : str, s2 : str) -> float:
    if not s and not s2:
        return 1.0

    numerator : int = 0
    n : int = 0

    while n < len(s) and n < len(s2):
        if s[n] == s2[n]:
            numerator += 1

        n += 1

    denominator : int = max(len(s), len(s2))

    return numerator / denominator

@pytest.mark.parametrize("parameter, expected", [
    (("", ""), 1.0),
    (("abc", ""), 0.0),
    (("", "efg"), 0.0),
    (("Python", "pYTHON"), 0.0),
    (("AbcD", "Abcdef"), 0.5),
    (("12344321", "12abcd12344321"), 0.14285714285714285),
    (("Exercices", "Exercice"), 0.8888888888888888)])
def test_find_similarity_score_between_two_strs(
        parameter : Tuple[str, str], expected : int) -> None:
    assert find_similarity_score_between_two_strs(*parameter) == expected
