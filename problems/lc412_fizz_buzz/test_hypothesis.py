import pytest
from hypothesis import given, strategies as st, settings
from problems.lc412_fizz_buzz.solution import Solution


def reference_fizzbuzz(n: int) -> list[str]:
    out = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            out.append("FizzBuzz")
        elif i % 3 == 0:
            out.append("Fizz")
        elif i % 5 == 0:
            out.append("Buzz")
        else:
            out.append(str(i))
    return out


@settings(max_examples=200)
@given(st.integers(min_value=1, max_value=500))
def test_property_matches_reference(n):
    assert Solution().fizzBuzz(n) == reference_fizzbuzz(n)


@settings(max_examples=200)
@given(st.integers(min_value=1, max_value=500))
def test_property_rules_hold(n):
    out = Solution().fizzBuzz(n)
    assert len(out) == n

    for i, s in enumerate(out, start=1):
        if i % 15 == 0:
            assert s == "FizzBuzz"
        elif i % 3 == 0:
            assert s == "Fizz"
        elif i % 5 == 0:
            assert s == "Buzz"
        else:
            assert s == str(i)


@settings(max_examples=50)
@given(st.integers(max_value=0))
def test_property_invalid_values_raise(n):
    with pytest.raises(ValueError):
        Solution().fizzBuzz(n)


@settings(max_examples=50)
@given(st.one_of(st.text(), st.floats(allow_nan=False), st.lists(st.integers())))
def test_property_invalid_types_raise(x):
    with pytest.raises(TypeError):
        Solution().fizzBuzz(x)