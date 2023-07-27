from typing import List
def arraySign(nums: List[int]) -> int:
    result = 1
    for i in nums:
        result *= i
    if result > 0 :
         return 1
    elif result == 0 :
        return 0
    else :
        return -1

# unit test arraySign
def test_arraySign():
    assert (arraySign([1, 5, 2, 3]) == 1)
    assert (arraySign([-1, -5, 0, -2, -3]) == 0)
    assert (arraySign([1, -5, 2, -3]) == 1)