from typing import List, Tuple
import sys
import pytest

def max_profit(profits : List[int]) -> Tuple[int, int]:
    if not profits:
        return (-1, -1)

    best_profit_begin_idx : int = 0
    best_profit_end_idx : int = 0
    best_profit : int = profits[0]
    n : int = 0

    while n < len(profits):
        current_profits_sum : int = profits[n]

        def try_set_best_profit_infos(n : int, n2 : int, current_profits_sum : int) -> None:
            nonlocal best_profit_begin_idx, best_profit_end_idx, best_profit

            if current_profits_sum > best_profit:
                best_profit_begin_idx = n
                best_profit_end_idx = n2
                best_profit = current_profits_sum

        try_set_best_profit_infos(n, n, current_profits_sum)

        n2 : int = n + 1

        while n2 < len(profits):
            current_profits_sum += profits[n2]
            try_set_best_profit_infos(n, n2, current_profits_sum)
            n2 += 1

        n += 1

    return best_profit_begin_idx, best_profit_end_idx

@pytest.mark.parametrize("parameter, expected", [
    ([], (-1, -1)),
    ([42], (0, 0)),
    ([-6, 2], (1, 1)),
    ([1, 3, 5, 3], (0, 3)),
    ([-2, 6, 5, -9], (1, 2))])
def test_max_profit(parameter : List[int], expected : Tuple[int, int]) -> None:
    assert max_profit(parameter) == expected
