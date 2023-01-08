#linked list 技巧

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def removeElements(head: ListNode, val: int) -> ListNode:
    #dummy 新增一個假的值 防止一開始的head是要刪掉的值
    dummy = ListNode(-1,head)
    curr = dummy
    while curr and curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next

#只能在leetcode 跑