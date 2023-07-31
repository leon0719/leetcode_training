from typing import List

# 這個函式 rotate 的目的是將列表 nums 向右旋轉 k 步。
# 1.numscopy = nums[:]: 這行將 nums 列表複製一份並賦值給 numscopy。
# 這是為了在進行旋轉操作時保留原始的 nums 列表，以免影響後續的索引計算。

# for i in range(len(nums)):
# 這是一個迴圈，它遍歷 nums 列表的每個元素。在每次迴圈運行時，我們將執行以下操作：
# nums[(i + k) % len(nums)] = numscopy[i]:
# 這行是旋轉操作的核心。它將 numscopy 中的元素按照 (i + k) % len(nums) 的索引位置放回到 nums 列表中。
# 這樣就完成了將 nums 向右旋轉 k 步的操作。

# 舉例來說，如果 nums = [1, 2, 3, 4, 5] 且 k = 2，則旋轉後的結果是 [4, 5, 1, 2, 3]。


def rotate(nums: List[int], k: int) -> None:
    numscopy = nums[:]
    for i in range(len(nums)):
        nums[(i + k) % len(nums)] = numscopy[i]


# unit test
def test_rotate():
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    rotate(nums, 2)
    assert nums == [3, 99, -1, -100]
