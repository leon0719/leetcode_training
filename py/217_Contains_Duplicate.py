from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    set_list = set(nums)
    if len(nums) != len(set_list):
        return True
    else:
        return False


if __name__ == "__main__":
    a = containsDuplicate([1, 2, 3, 1])
    print(a)
