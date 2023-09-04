# 0. 首先若 len(arr) <= 1 時必須return 陣列本身arr
# 1. 先找出陣列中間點  pivot
# 2. left 為 小於 陣列中間點的所有元素
# 3. right 為 大於 陣列中間點的所有元素
# return 遞迴QuickSort(left) + middle + QuickSort(right)


def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return QuickSort(left) + middle + QuickSort(right)


if __name__ == "__main__":
    arr = [32, 4, 77, 15, 22, 56]
    print(QuickSort(arr))
