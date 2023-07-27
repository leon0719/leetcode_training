from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

#unit test hasCycle
def test_hasCycle():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next # ListNode(2)
    assert (hasCycle(head) == True)
    head.next.next.next.next = head.next.next
    assert (hasCycle(head) == True)
    head.next.next.next.next = None
    assert (hasCycle(head) == False)
