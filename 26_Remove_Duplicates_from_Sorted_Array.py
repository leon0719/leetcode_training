from typing import List
#題目輸入一個由小到大排序的陣列，
#我們需要回傳『沒有重複元素陣列長度』
#並將這些沒有重複的元素移動至該陣列的開頭。

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
