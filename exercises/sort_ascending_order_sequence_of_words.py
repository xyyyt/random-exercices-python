import pytest

def sort_ascending_order_sequence_of_words(s : str) -> str:
    return ", ".join(sorted(set(s.split(", "))))

@pytest.mark.parametrize("parameter, expected", [
    ("", ""),
    ("abcdef", "abcdef"),
    ("I'm here !!!", "I'm here !!!"),
    ("one, two, three", "one, three, two"),
    ("red, white, black, red, green, black", "black, green, red, white")])
def test_sort_ascending_order_sequence_of_words(
        parameter : str, expected : str) -> None:
    assert sort_ascending_order_sequence_of_words(parameter) == expected
