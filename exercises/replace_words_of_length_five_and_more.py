import pytest

def replace_words_of_length_five_and_more(s : str) -> str:
    if not s:
        return ""

    modified_str : str = ""
    n : int = 0

    while n < len(s):
        if s[n].isalpha():
            word_begin_pos : int = n

            while n < len(s) and s[n].isalpha():
                n += 1

            LENGTH_TO_REPLACE : int = 5
            word_length : int = n - word_begin_pos

            if word_length >= LENGTH_TO_REPLACE:
                CHARACTER_TO_USE_FOR_REPLACE = '#'

                modified_str += '#' * word_length
            else:
                modified_str += s[word_begin_pos:n]
        else:
            word_begin_pos = n

            while n < len(s) and not s[n].isalpha():
                n += 1

            modified_str += s[word_begin_pos:n]

    return modified_str

@pytest.mark.parametrize("parameter, expected", [
    ("",
     ""),
    ("  Count the    lowercase letters  in the     said  list of  words   ",
     "  ##### the    ######### #######  in the     said  list of  #####   "),
    ("     Python  - 123456  Remove   punctuations   from    a string",
     "     ######  - 123456  ######   ############   from    a ######")])
def test_replace_words_of_length_five_and_more(
        parameter : str, expected : str) -> None:
    assert replace_words_of_length_five_and_more(parameter) == expected
