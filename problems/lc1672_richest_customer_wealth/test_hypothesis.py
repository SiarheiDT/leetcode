from hypothesis import given, strategies as st
from problems.lc1672_richest_customer_wealth.solution import Solution

@given(
    st.lists(
        st.lists(st.integers(min_value=0, max_value=10_000), min_size=1, max_size=20),
        min_size=1,
        max_size=50,
    )
)
def test_property(accounts):
    expected = max(map(sum, accounts))
    assert Solution().maximumWealth(accounts) == expected