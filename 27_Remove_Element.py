from typing import List
def removeElement(nums: List[int], val: int) -> int:
    if len(nums) == 0:
        return len(nums)
    elif val not in nums:
        return len(nums)
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count


if __name__ == "__main__":
    test1=[3,2,2,3]
    val1 = 3
    print(removeElement(test1,val1))
