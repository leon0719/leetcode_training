from typing import List

def removeDuplicates(nums: List[int]) -> int:
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            nums.remove(nums[i])
            i -= 1
        i += 1

    return len(nums)

if __name__ == "__main__":
    test1 = [0,0,1,1,1,2,2,3,3,4]

    print(removeDuplicates(test1))
