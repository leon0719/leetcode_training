class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        node.next, node.val = node.next.next, node.next.val


# 只能在leetcode跑
