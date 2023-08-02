from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # root 要進入的節點
    # inorder_list 最終要回傳的list
    def traversal(self, root: TreeNode, inorder_list: List[int]):
        # 沒有節點往回走
        if root is None:
            return inorder_list
        # 前往左邊子節點
        inorder_list = self.traversal(root.left, inorder_list)
        # 左邊子節點回來以後，將目前節點的值紀錄到list中
        inorder_list.append(root.val)
        # 前往右邊子節點
        inorder_list = self.traversal(root.right, inorder_list)
        return inorder_list

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.traversal(root, [])


# unit test


def test_inorderTraversal():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    solution = Solution()  # 創建 Solution 實例
    result = solution.inorderTraversal(root)  # 通過實例調用 inorderTraversal 方法
    assert result == [1, 3, 2]
