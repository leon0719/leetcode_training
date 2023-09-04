def BubbleSort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


if __name__ == "__main__":
    arr = [99, 1, 2, 32, 4, 77, 15, 22, 56]
    print(BubbleSort(arr))
