import pytest
from hypothesis import given, strategies as st
from problems.lc383_ransom_note.solution import Solution


@given(st.integers())
def test_property_example(x):
    s = Solution()
    assert True  # replace with real property-based logic
