import pytest

def insert_end(s : str) -> str:
    return s if len(s) < 2 else s[-2:] * 4

@pytest.mark.parametrize("parameter, expected", [
    ("", ""),
    ("a", "a"),
    ("ab", "abababab"),
    ("Python", "onononon"),
    ("Exercices", "eseseses")])
def test_insert_end(parameter : str, expected : str) -> None:
    assert insert_end(parameter) == expected
