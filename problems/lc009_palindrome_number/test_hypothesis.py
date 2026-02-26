import pytest
from hypothesis import given, strategies as st, settings
from problems.lc009_palindrome_number.solution import Solution


# -------------------------
# Reference implementation
# -------------------------

def reference_is_palindrome(x: int) -> bool:
    # Поведение как в твоём коде:
    if not isinstance(x, int):
        raise TypeError
    if x < 0:
        raise ValueError
    s = str(x)
    return s == s[::-1]


# -------------------------
# Property tests
# -------------------------

@settings(max_examples=300)
@given(st.integers(min_value=0, max_value=10**10))
def test_matches_reference_for_non_negative_integers(x):
    assert Solution().isPalindrome(x) == reference_is_palindrome(x)


@settings(max_examples=200)
@given(st.integers(min_value=-10**6, max_value=-1))
def test_negative_numbers_raise_value_error(x):
    with pytest.raises(ValueError):
        Solution().isPalindrome(x)


@settings(max_examples=200)
@given(
    st.one_of(
        st.text(),
        st.floats(allow_nan=False),
        st.lists(st.integers()),
        st.none(),
    )
)
def test_non_integer_inputs_raise_type_error(x):
    with pytest.raises(TypeError):
        Solution().isPalindrome(x)


@settings(max_examples=200)
@given(st.integers(min_value=0, max_value=10**10))
def test_single_digit_always_palindrome(x):
    # если число однозначное → всегда палиндром
    if 0 <= x < 10:
        assert Solution().isPalindrome(x) is True