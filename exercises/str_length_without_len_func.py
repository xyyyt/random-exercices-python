import pytest

def recursive_str_length_without_len_func(s : str) -> int:
    def calculate_length(s : str, n : int) -> int:
        return 1 + calculate_length(s, n + 1) if n < len(s) else 0

    return calculate_length(s, 0)

def iterative_str_length_without_len_func(s : str) -> int:
    length : int = 0

    for c in s:
        length += 1

    return length

class TestParametrized:
    _COMMON_ARGS = ("parameter, expected", [
        ("", 0),
        ("a", 1),
        ("ab", 2),
        ("abc", 3),
        ("abcd", 4)])

    @pytest.mark.parametrize(*_COMMON_ARGS)
    def test_iterative_str_length_without_len_func(
            self, parameter : str, expected : int) -> None:
        assert iterative_str_length_without_len_func(parameter) == expected

    @pytest.mark.parametrize(*_COMMON_ARGS)
    def test_recursive_str_length_without_len_func(
            self, parameter : str, expected : int) -> None:
        assert recursive_str_length_without_len_func(parameter) == expected
