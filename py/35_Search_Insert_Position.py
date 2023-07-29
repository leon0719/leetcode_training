from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left


def test_searchInsert():
    assert searchInsert([1, 3, 5, 6], 5) == 2
    print("All tests passed!")


def test_searchInsert2():
    assert searchInsert([1, 3, 5, 6], 2) == 1
    print("All tests passed!")


def test_searchInsert3():
    assert searchInsert([1, 3, 5, 6], 7) == 4
    print("All tests passed!")
