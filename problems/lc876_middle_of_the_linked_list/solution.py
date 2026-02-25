from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# -------------------------
# Utility functions
# -------------------------

def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def print_linked_list(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    return " -> ".join(values)


# -------------------------
# Example run
# -------------------------

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]

    head = build_linked_list(data)

    print("Input list:")
    print(print_linked_list(head))

    middle = Solution().middleNode(head)

    print("\nMiddle node onward:")
    print(print_linked_list(middle))