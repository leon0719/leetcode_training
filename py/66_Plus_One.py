from typing import List

def plusOne(digits: List[int]) -> List[int]:
    return [int(i) for i in str(int(''.join([str(i) for i in digits]))+1)]



    # return [int(i) for i in str(int(''.join(str(dig) for dig in digits))+1)]


# unit test plusOne

def test_plusOne():
    assert (plusOne([1, 2, 3]) == [1, 2, 4])
    assert (plusOne([4, 3, 2, 1]) == [4, 3, 2, 2])
    assert (plusOne([0]) == [1])
    assert (plusOne([9]) == [1, 0])
    assert (plusOne([9, 9]) == [1, 0, 0])
    assert (plusOne([9, 9, 9]) == [1, 0, 0, 0])
    assert (plusOne([9, 9, 9, 9]) == [1, 0, 0, 0, 0])
    assert (plusOne([9, 9, 9, 9, 9]) == [1, 0, 0, 0, 0, 0])
    assert (plusOne([9, 9, 9, 9, 9, 9]) == [1, 0, 0, 0, 0, 0, 0])
    assert (plusOne([9, 9, 9, 9, 9, 9, 9]) == [1, 0, 0, 0, 0, 0, 0, 0])