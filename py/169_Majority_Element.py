from typing import List


# 目的是找出在給定的整數列表 nums 中出現次數超過一半的主要元素，並返回該主要元素的值
# 是先對 nums 進行排序，然後返回排在中間位置的元素值。因為這是一個已排序的列表，
# 而主要元素出現次數超過一半，所以中間位置的元素必然是主要元素。


def majorityElement(nums: List[int]) -> int:
    return sorted(nums)[len(nums) // 2]


# unit test
def test_majorityElement():
    assert majorityElement([3, 2, 3]) == 3
    assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
