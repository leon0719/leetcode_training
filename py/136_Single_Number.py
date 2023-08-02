from typing import List


def singleNumber(nums: List[int]) -> int:
    xor = 0
    for num in nums:
        print("xor", xor)
        xor ^= num
    return xor


if __name__ == "__main__":
    print(singleNumber([1, 7, 4, 1, 7]))
