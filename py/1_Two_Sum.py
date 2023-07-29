from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}
    for i in range(len(nums)):
        temp = target - nums[i]
        if temp not in hashmap:
            hashmap[nums[i]] = i
        else:
            return [hashmap[temp], i]


def test_twoSum():
    # unit test twoSum
    nums = [2, 7, 11, 15]
    target = 9
    assert twoSum(nums, target) == [0, 1]
    print("Pass")
    print("---------------------")


def test_twoSum2():
    # unit test twoSum
    nums = [3, 2, 4]
    target = 6
    assert twoSum(nums, target) == [1, 2]
    print("Pass")
    print("---------------------")
