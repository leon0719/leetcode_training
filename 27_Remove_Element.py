from typing import List
def removeElement(nums: List[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


# unit test removeElement

def test_removeElement():
    nums = [3,2,2,3]
    val = 3
    assert (removeElement(nums, val) == 2)
    

