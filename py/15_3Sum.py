from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    v = set()
    target = 0
    for i in range(len(nums)):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            addNum = nums[i] + nums[j] + nums[k]
            if addNum == target:
                v.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            else:
                if addNum < target:
                    j += 1
                else:
                    k -= 1
    return list(list(v))


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))
