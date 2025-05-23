import pytest

def capitalize_first_letter_and_lowercases_remaining_letters(s : str) -> str:
    if not s:
        return ""

    modified_str : str = ""
    n : int = 0

    while n < len(s):
        if s[n].isalpha() or s[n].isnumeric():
            word_begin_pos : int = n

            while n < len(s) and (s[n].isalpha() or s[n].isnumeric()):
                n += 1

            modified_str += s[word_begin_pos].upper()
            word_begin_pos += 1

            while word_begin_pos < n:
                modified_str += s[word_begin_pos].lower()
                word_begin_pos += 1
        else:
            word_begin_pos = n

            while n < len(s) and not (s[n].isalpha() or s[n].isnumeric()):
                n += 1

            modified_str += s[word_begin_pos:n]

    return modified_str

@pytest.mark.parametrize("parameter, expected", [
    ("", ""),
    ("Red    Green   WHITE", "Red    Green   White"),
    (" w3resource", " W3resource"),
    ("  dow jones industrial  average 42  ", "  Dow Jones Industrial  Average 42  ")])
def test_capitalize_first_letter_and_lowercases_remaining_letters(
        parameter : str, expected : str) -> None:
     assert capitalize_first_letter_and_lowercases_remaining_letters(
         parameter) == expected
