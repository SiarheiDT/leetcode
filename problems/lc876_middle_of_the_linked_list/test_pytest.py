from typing import Optional, List
from problems.lc876_middle_of_the_linked_list.solution import Solution, ListNode


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


def test_odd_length():
    head = build_linked_list([1, 2, 3, 4, 5])
    mid = Solution().middleNode(head)
    assert linked_list_to_list(mid) == [3, 4, 5]


def test_even_length_second_middle():
    head = build_linked_list([1, 2, 3, 4, 5, 6])
    mid = Solution().middleNode(head)
    assert linked_list_to_list(mid) == [4, 5, 6]


def test_single_node():
    head = build_linked_list([7])
    mid = Solution().middleNode(head)
    assert linked_list_to_list(mid) == [7]


def test_two_nodes_returns_second():
    head = build_linked_list([10, 20])
    mid = Solution().middleNode(head)
    assert linked_list_to_list(mid) == [20]


def test_three_nodes_returns_second():
    head = build_linked_list([10, 20, 30])
    mid = Solution().middleNode(head)
    assert linked_list_to_list(mid) == [20, 30]


def test_large_list():
    head = build_linked_list(list(range(1, 101)))  # 1..100 (even)
    mid = Solution().middleNode(head)
    assert linked_list_to_list(mid) == list(range(51, 101))  # second middle is 51