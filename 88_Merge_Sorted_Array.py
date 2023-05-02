from typing import List
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    P1, P2, P3 = m - 1, n - 1, m + n -1
    while P1 >= 0 and P2 >= 0 :
        if nums1[P1] >= nums2[P2]:
            nums1[P3] = nums1[P1]
            P1 -= 1
        else:
            nums1[P3] = nums2[P2]
            P2 -= 1
        P3 -= 1
    while P2 >= 0 :
        nums1[P3] = nums2[P2]
        P2 -=1
        P3 -=1


#unit test Merge Sorted Array
def test_merge_sorted_array():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)
    assert (nums1 == [1, 2, 2, 3, 5, 6])