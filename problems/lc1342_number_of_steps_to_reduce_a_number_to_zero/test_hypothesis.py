from hypothesis import given, strategies as st, settings
from problems.lc1342_number_of_steps_to_reduce_a_number_to_zero.solution import Solution


def reference(num: int) -> int:
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num //= 2
        else:
            num -= 1
        steps += 1
    return steps


@settings(max_examples=200)
@given(st.integers(min_value=0, max_value=10_000))
def test_matches_reference(num):
    assert Solution().numberOfSteps(num) == reference(num)


@settings(max_examples=200)
@given(st.integers(min_value=0, max_value=10_000))
def test_result_non_negative(num):
    result = Solution().numberOfSteps(num)
    assert result >= 0


@settings(max_examples=200)
@given(st.integers(min_value=1, max_value=10_000))
def test_reduces_to_zero(num):
    steps = Solution().numberOfSteps(num)

    # theoretical upper bound:
    # max steps < 2 * number_of_bits
    bit_length = num.bit_length()
    assert steps <= bit_length * 2