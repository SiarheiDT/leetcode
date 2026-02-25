from typing import Optional, List
import pytest
from hypothesis import given, strategies as st, settings

from problems.lc876_middle_of_the_linked_list.solution import Solution, ListNode


# -------------------------
# Helpers
# -------------------------

def build_linked_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def reference_middle(values: List[int]) -> List[int]:
    mid_index = len(values) // 2
    return values[mid_index:]


# -------------------------
# Property tests
# -------------------------

@settings(max_examples=200)
@given(
    st.lists(
        st.integers(min_value=-1000, max_value=1000),
        min_size=1,
        max_size=200,
    )
)
def test_middle_matches_reference(values):
    head = build_linked_list(values)
    result_node = Solution().middleNode(head)
    result_list = linked_list_to_list(result_node)

    assert result_list == reference_middle(values)


@settings(max_examples=200)
@given(
    st.lists(
        st.integers(),
        min_size=1,
        max_size=200,
    )
)
def test_length_of_result(values):
    head = build_linked_list(values)
    result_node = Solution().middleNode(head)
    result_list = linked_list_to_list(result_node)

    # Result length must be ceil(n/2)
    assert len(result_list) == len(values) - (len(values) // 2)