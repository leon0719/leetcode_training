from typing import List
def searchInsert(nums: List[int], target: int) -> int:
    left,right = 0,len(nums)-1
    while left <= right:
        mid = (left + right) //2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return left



if __name__ == "__main__":
    test1 = [1,3,5,6]
    target = 7
    print(searchInsert(test1, target))