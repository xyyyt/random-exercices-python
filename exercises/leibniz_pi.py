import pytest

def leibniz_pi(term_nb : int) -> float:
    pi_on_four : float = 1 - (1 / 3) + (1 / 5) - (1 / 7) + (1 / 9)
    denominator : int = 11

    for _ in range(term_nb):
        pi_on_four = pi_on_four - (1 / denominator) + (1 / (denominator + 2))
        denominator += 4

    return 4.0 * pi_on_four

@pytest.mark.parametrize("parameter, expected", [
    (0, 3.3396825396825403),
    (2, 3.2523659347188767),
    (5, 3.208185652261944)])
def test_leibniz_pi(parameter : int, expected : float) -> None:
    assert leibniz_pi(parameter) == expected
