from typing import List


def maxArea(height: List[int]) -> int:
    max_area = 0
    left = 0
    right = len(height) - 1
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
            continue  # continue 後 跳過當前迴圈迭代，進行下一次迭代
        right -= 1
    return max_area


if __name__ == "__main__":
    # unit test
    print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
