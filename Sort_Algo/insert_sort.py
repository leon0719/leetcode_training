def InsertSort(arr):
    n = len(arr)
    for i in range(n - 1):
        key = arr[i + 1]
        j = i
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    arr = [72, 1, -7, -1, 2, 5, 8, 4]
    print(InsertSort(arr))
