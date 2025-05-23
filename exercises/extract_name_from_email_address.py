import pytest

def extract_name_from_email_address(s : str) -> str:
    if not s:
        raise ValueError("Email address is empty")

    try:
        at_sign_pos : int = s.index('@')
    except ValueError:
        raise ValueError("Missing at sign character")
    else:
        name : str = ""

        for n in range(0, at_sign_pos):
            if s[n].isalpha() or s[n].isnumeric():
                name += s[n]

    return name

@pytest.mark.parametrize("parameter", [
    (""),
    ("abcdefghaa9dqsdqs"),
    ("klsqmqs???!!!%ada"),
    ("1234567]][[()abc")])
def test_extract_name_from_email_address__errors(parameter : str) -> None:
    with pytest.raises(ValueError):
        extract_name_from_email_address(parameter)

@pytest.mark.parametrize("parameter, expected", [
    ("john@example.com", "john"),
    ("john.smith42@example.com", "johnsmith42"),
    ("fully-qualified-domain@example.com", "fullyqualifieddomain")])
def test_extract_name_from_email_address(parameter : str, expected : str) -> None:
    assert extract_name_from_email_address(parameter) == expected
