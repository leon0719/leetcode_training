# 1.for loop i 遍歷 整個陣列
# 2.for loop j 遍歷 1到 整個陣列 - i (重要)
# 3. 比大小


def BubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
    return arr


if __name__ == "__main__":
    arr = [99, 1, 2, 32, 4, 77, 15, 22, 56]
    print(BubbleSort(arr))
