import pytest

def sort_str_lexicographically(s : str) -> str:
    return "".join(sorted(list(s)))

@pytest.mark.parametrize("parameter, expected", [
    ("", ""),
    ("abcd", "abcd"),
    ("dcba", "abcd"),
    ("tsrq", "qrst")])
def test_sort_str_lexicographically(parameter : str, expected : str) -> None:
    assert sort_str_lexicographically(parameter) == expected
