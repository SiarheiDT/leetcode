import pytest
from problems.lc383_ransom_note.solution import Solution


@pytest.mark.parametrize(
    "ransom, magazine, expected",
    [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("", "", True),                 # empty ransom is always constructible
        ("", "abc", True),
        ("abc", "", False),
        ("a", "a", True),
        ("b", "bbb", True),
        ("abc", "cba", True),
        ("abc", "ab", False),
        ("zzz", "zzzz", True),
        ("zzy", "zzz", False),
    ],
)
def test_can_construct_cases(ransom, magazine, expected):
    assert Solution().canConstruct(ransom, magazine) is expected


def test_len_ransom_greater_than_magazine_fast_fail():
    assert Solution().canConstruct("abcd", "abc") is False


def test_repeated_letters_exact_match():
    assert Solution().canConstruct("aaab", "baaa") is True
    assert Solution().canConstruct("aaabb", "baaa") is False