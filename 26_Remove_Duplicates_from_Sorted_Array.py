from typing import List

def removeDuplicates(nums: List[int]) -> int:
    count = 1
    while count < len(nums):
        if nums[count] == nums[count - 1]:
            nums.pop(count)
        else:
            count += 1
    return count



# unit test removeDuplicates

def test_removeDuplicates():
    nums = [1, 1, 2]
    assert (removeDuplicates(nums) == 2)
    assert (nums == [1, 2])

def test_removeDuplicates2():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert (removeDuplicates(nums) == 5)
    assert (nums == [0, 1, 2, 3, 4])