from typing import List
import pysnooper
#題目輸入一個由小到大排序的陣列，
#我們需要回傳『沒有重複元素陣列長度』
#並將這些沒有重複的元素移動至該陣列的開頭。
@pysnooper.snoop()
def removeDuplicates(nums: List[int]) -> int:
    index = 0
    for i in range(len(nums)):
        if (i == 0 or nums[i] != nums[i-1]):
            nums[index] = nums[i]
            index += 1

    return index


if __name__ == "__main__":
    test1 = [0,0,1,1,1,2,2,3,3,4]

    print(removeDuplicates(test1))
