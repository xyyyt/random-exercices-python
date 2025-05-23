from typing import Tuple
import pytest

def get_last_part_of_the_str_before_char(s : str, c : str) -> str:
    idx : int = s.rfind(c)

    return s if idx == -1 else s[idx + len(c):]

@pytest.mark.parametrize("parameter, expected", [
    (("Hello World !", '?'), "Hello World !"),
    (("https://www.w3resource.com/python-exercises", '/'), "python-exercises"),
    (("https://www.w3resource.com/python", "www"), ".w3resource.com/python")])
def test_get_last_part_of_the_str_before_char(
        parameter : Tuple[str, str], expected : str) -> None:
    assert get_last_part_of_the_str_before_char(*parameter) == expected
