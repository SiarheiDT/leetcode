import pytest
from problems.lc009_palindrome_number.solution import Solution


@pytest.mark.parametrize(
    "x, expected",
    [
        (0, True),
        (1, True),
        (5, True),
        (11, True),
        (121, True),
        (1221, True),
        (12321, True),
        (10, False),
        (12, False),
        (123, False),
        (1231, False),
        (1001, True),
        (100, False),
    ],
)
def test_palindrome_valid_cases(x, expected):
    assert Solution().isPalindrome(x) is expected


def test_large_palindrome():
    x = 123454321
    assert Solution().isPalindrome(x) is True


def test_large_non_palindrome():
    x = 123456789
    assert Solution().isPalindrome(x) is False


# ---- Validation tests ----

def test_negative_number_raises_value_error():
    with pytest.raises(ValueError):
        Solution().isPalindrome(-121)


def test_non_integer_input_raises_type_error():
    with pytest.raises(TypeError):
        Solution().isPalindrome("121")

    with pytest.raises(TypeError):
        Solution().isPalindrome(12.1)

    with pytest.raises(TypeError):
        Solution().isPalindrome(None)