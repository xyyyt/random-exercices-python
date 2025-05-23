from typing import Tuple
from queue import PriorityQueue
import pytest

def find_longest_common_substr(s : str, s2 : str) -> str:
    if not s or not s2:
        return ""

    p_queue : PriorityQueue[Tuple[int, str]] = PriorityQueue()

    for n in range(0, len(s)):
        for n2 in range(0, len(s2)):
            if s[n] == s2[n2]:
                n3 : int = n
                n4 : int = n2

                while n3 < len(s) and n4 < len(s2) and s[n3] == s2[n4]:
                    n3 += 1
                    n4 += 1

                substr : str = s[n:n3]

                p_queue.put_nowait((-len(substr), substr))

    return "" if p_queue.empty() else p_queue.get_nowait()[1]

@pytest.mark.parametrize("parameter, expected", [
    (("", ""), ""),
    (("abcd", ""), ""),
    (("", "efgh"), ""),
    (("abc", "aaaaabbbera"), "ab"),
    (("abbbba", "tydfsbdqssbbqsbbb"), "bbb"),
    (("abcdefgh", "xswerabcdwd"), "abcd"),
    (("afghahadqdsdjk", "phpqsdhadgfqhahahdqdk"), "haha")])
def test_find_longest_common_substr(
        parameter : Tuple[str, str], expected : str) -> None:
    assert find_longest_common_substr(*parameter) == expected
