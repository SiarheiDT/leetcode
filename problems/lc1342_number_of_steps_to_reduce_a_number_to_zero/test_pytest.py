import pytest
from problems.lc1342_number_of_steps_to_reduce_a_number_to_zero.solution import Solution


@pytest.mark.parametrize(
    "num, expected",
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (8, 4),
        (14, 6),
        (123, 12),
        (1024, 11),
    ],
)
def test_known_cases(num, expected):
    assert Solution().numberOfSteps(num) == expected


def test_large_power_of_two():
    # 2^10 = 1024 -> 10 divisions + 1 subtraction
    assert Solution().numberOfSteps(1024) == 11


def test_zero():
    assert Solution().numberOfSteps(0) == 0