from typing import List, Tuple
import pytest

def is_point_in_circle(x : float, y : float) -> bool:
    return (x ** 2 + y ** 2) < 1.0

def geometrically_pi_estimation(x_y_coordinates : List[Tuple[float, float]]) -> float:
    acc : int = 0

    for x, y in x_y_coordinates:
        if is_point_in_circle(x, y):
            acc += 1

    return 4.0 * acc / len(x_y_coordinates)

@pytest.mark.parametrize("parameter, expected", [
    ([(0.12, 0.99), (0.99, 0.99), (0.86, 0.92), (0.76, 0.82)], 1.0),
    ([(0.32, 0.92), (0.05, 0.24), (0.01, 0.04), (0.25, 0.21), (0.50, 0.25)], 4.0),
    ([(0.51, 0.27), (0.19, 0.83), (0.41, 0.81), (0.02, 0.34), (0.98, 0.96)], 3.2)])
def test_geometrically_pi_estimation(
        parameter : List[Tuple[float, float]], expected : float) -> None:
    assert geometrically_pi_estimation(parameter) == expected
