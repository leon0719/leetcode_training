from typing import List

test1 = [2,7,11,15,4,5]
target1 = 7
test2 = [3,2,4,7,8]
target2 = 15
test3 = [3,3]
target3 = 6

def twoSum(nums: List[int], target: int) -> List[int]:
    hashtable = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement not in hashtable:
            hashtable[nums[i]] = i
        else:
            print(hashtable)
            return [hashtable[complement], i]
    return None



if __name__ == "__main__":
    print(twoSum(test1,target1))


