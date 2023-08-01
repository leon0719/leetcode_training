from typing import List

"""
Input: nums = [2, 3, 1, 1, 4]
Output: true

1. 在 index 0 你可以跳2步也可以跳1步
若跳2步到達 index 2 再來跳 1步 到 index 3
跳到 index 3 需要跳1步才能到 index 4 因此可以到達

2. 若從 index 0 開始跳1步 到 index 1 跳3步到 index 4 也可以


###############
創建一個變數 maxReach 並初始化為 0。這個變數用於記錄目前所能達到的最遠位置。

1. 使用一個迴圈遍歷列表 nums 中的每個元素，迴圈的索引為 i。

2. 在迴圈的每次迭代中，先檢查當前位置 i 是否已經超過了 maxReach。
如果 i > maxReach，表示無法再向前跳躍，直接返回 False，表示無法成功跳躍到最後一個位置。

3. 如果 i <= maxReach，則更新 maxReach 為當前位置 i 能夠跳到的最遠位置 i + nums[i]。
這裡的 nums[i] 是當前位置 i 能夠跳的最大步數。

4. 迴圈遍歷完成後，如果 maxReach 大於或等於最後一個位置的索引 len(nums) - 1，
則表示可以成功跳躍到最後一個位置，函式返回 True；否則，表示無法成功跳躍到最後一個位置，函式返回 False。
"""


def canJump(nums: List[int]) -> bool:
    maxReach = 0
    for i in range(len(nums)):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + nums[i])
    return True


# test


if __name__ == "__main__":
    nums = [3, 2, 1, 0, 4]
    print(canJump(nums))
