from typing import List
import pytest

def integer_triangle(n : int) -> str:
    l : List[str] = []

    for i in range(1, n + 1):
        l2 : List[str] = []

        for j in range(1, i + 1):
            l2.append(str(i))

        l.append(''.join(l2))

    return '\n'.join(l)

@pytest.mark.parametrize("parameter, expected", [
    (0, ""),
    (1, "1"),
    (2, "1\n22"),
    (3, "1\n22\n333"),
    (4, "1\n22\n333\n4444")])
def test_integer_triangle(parameter : int, expected : str) -> None:
    assert integer_triangle(parameter) == expected
