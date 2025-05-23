from typing import Tuple
import pytest

def find_nb_occurrence(s : str, text_to_find : str) -> int:
    if not s:
        raise ValueError("string cannot be empty")
    elif not text_to_find:
        return 0

    nb_occurrence : int = 0
    n : int = 0

    while n < len(s):
        if s[n] == text_to_find[0]:
            n2 : int = 0

            while n < len(s) \
                  and n2 < len(text_to_find) \
                  and s[n] == text_to_find[n2]:
                n += 1
                n2 += 1

            if n2 == len(text_to_find):
                nb_occurrence += 1
        else:
            n += 1

    return nb_occurrence

def test_find_nb_occurrence_without_text() -> None:
    with pytest.raises(ValueError):
        find_nb_occurrence("", "abcd")

@pytest.mark.parametrize("parameter, expected", [
    (("Loupa loumpi", ""), 0),
    (("Loupa loumpi", "L"), 1),
    (("Loupa loumpi", "mpi"), 1),
    (("Loupa loumpi", "ou"), 2),
    (("hello hallo hello", ""), 0),
    (("hello hallo hello", "all"), 1),
    (("hello hallo hello", "hello"), 2),
    (("hello hallo hello", "ll"), 3),
    (("hello hallo hello", "l"), 6)])
def test_find_nb_occurrence_with_text(
        parameter : Tuple[str, str], expected : int) -> None:
    assert find_nb_occurrence(*parameter) == expected
