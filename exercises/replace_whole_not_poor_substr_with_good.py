from typing import Tuple, List
from queue import Queue
import pytest

def replace_whole_not_poor_substr_with_good(s : str) -> str:
    start_end_indexes : Queue[Tuple[int, int]] = Queue()
    start : int = 0

    while True:
        SUBSTR_START : str = "not"

        start = s.find(SUBSTR_START, start)

        if start == -1:
            break

        SUBSTR_END : str = "poor"
        end : int = s.find(SUBSTR_END, start + len(SUBSTR_START))

        if end != -1:
            start_end_indexes.put_nowait((start, end + len(SUBSTR_END)))
            start = end + len(SUBSTR_END) + 1
        else:
            start = start + len(SUBSTR_START) + 1

    substrs : List[str] = []
    index : int = 0

    while not start_end_indexes.empty():
        start, end = start_end_indexes.get_nowait()
        substrs.append(s[index:start])
        substrs.append("good")
        index = end

    substrs.append(s[index:])

    return "".join(substrs)

@pytest.mark.parametrize("parameter, expected", [
    ("", ""),
    ("Hello World !", "Hello World !"),
    ("The lyrics is not that poor! The lyrics is poor!",
     "The lyrics is good! The lyrics is poor!"),
    ("Food is not not not poor !", "Food is good !")])
def test_replace_whole_not_poor_substr_with_good(
        parameter : str, expected : str) -> None:
    assert replace_whole_not_poor_substr_with_good(parameter) == expected
