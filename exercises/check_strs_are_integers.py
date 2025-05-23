from typing import Tuple, Callable
import pytest

def check_strs_are_integers(s : str, s2 : str) -> str:
    msg_formatter_str_empty : Callable[[str], str] = \
        lambda s: f"\"{s}\" parameter is empty"

    if not s:
        return msg_formatter_str_empty('s')
    elif not s2:
        return msg_formatter_str_empty('s2')

    check_str_is_integer : Callable[[str], bool] = \
        lambda s: s[1:].isdigit() if s.startswith('-') else s.isdigit()
    msg_formatter : Callable[[str], str] = \
        lambda s: f"\"{s}\" is not a integer"

    stripped_s : str = s.strip()
    stripped_s2 : str = s2.strip()

    if not check_str_is_integer(stripped_s):
        return msg_formatter(s)
    elif not check_str_is_integer(stripped_s2):
        return msg_formatter(s2)
    else:
        return f"\"{s}\" and \"{s2}\" are integers"

@pytest.mark.parametrize("parameter, expected", [
    (("", ""), "\"s\" parameter is empty"),
    (("12", ""), "\"s2\" parameter is empty"),
    (("    ab   cd   ", "   42"), "\"    ab   cd   \" is not a integer"),
    (("42     ", "abcd"), "\"abcd\" is not a integer"),
    (("6   3", " 4   1   "), "\"6   3\" is not a integer"),
    ((" -1.2", "0"), "\" -1.2\" is not a integer"),
    ((" 3", "--0"), "\"--0\" is not a integer"),
    (("  -99999.0", "42.0"), "\"  -99999.0\" is not a integer"),
    (("  1   ", "321"), "\"  1   \" and \"321\" are integers"),
    (("0  ", "  0"), "\"0  \" and \"  0\" are integers"),
    ((" -34", "    59"), "\" -34\" and \"    59\" are integers"),
    (("0", "1"), "\"0\" and \"1\" are integers"),
    (("4", "   -999999   "), "\"4\" and \"   -999999   \" are integers")])
def test_check_strs_are_integers(parameter : Tuple[str, str], expected : str) -> None:
    assert check_strs_are_integers(*parameter) == expected
