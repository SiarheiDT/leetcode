from collections import Counter
import pytest
from hypothesis import given, strategies as st, settings

from problems.lc383_ransom_note.solution import Solution


alphabet = st.characters(min_codepoint=ord("a"), max_codepoint=ord("z"))
lower_str = st.text(alphabet=alphabet, min_size=0, max_size=200)


def reference_can_construct(ransom: str, magazine: str) -> bool:
    # Reference using Counter (trusted baseline)
    rc = Counter(ransom)
    mc = Counter(magazine)
    for ch, need in rc.items():
        if mc[ch] < need:
            return False
    return True


@settings(max_examples=300)
@given(ransom=lower_str, magazine=lower_str)
def test_matches_reference_counter(ransom, magazine):
    assert Solution().canConstruct(ransom, magazine) == reference_can_construct(ransom, magazine)


@settings(max_examples=200)
@given(magazine=lower_str)
def test_ransom_empty_always_true(magazine):
    assert Solution().canConstruct("", magazine) is True


@settings(max_examples=200)
@given(ransom=lower_str, magazine=lower_str)
def test_len_rule_if_ransom_longer_then_false(ransom, magazine):
    if len(ransom) > len(magazine):
        assert Solution().canConstruct(ransom, magazine) is False