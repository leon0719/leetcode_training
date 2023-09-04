from typing import List

# 動態規劃 dynamic programming


test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
test2 = [1]
test3 = [5, 4, -1, 7, 8]


def maxSubArray(s: List) -> int:
    if not s:
        return 0
    length_list = len(s)
    sub_sum, sub_max = s[0], s[0]
    for i in range(1, length_list):
        sub_sum = max(sub_sum + s[i], s[i])
        sub_max = max(sub_sum, sub_max)
    return sub_max


if __name__ == "__main__":
    print(maxSubArray(test1))
