def MergeSort(arr):
    if len(arr) > 1:
        r = len(arr) // 2
        L = arr[:r]
        R = arr[r:]
        MergeSort(L)
        MergeSort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


if __name__ == "__main__":
    arr = [5, 3, 8, 6, 2, 7, 1, 4]
    print(MergeSort(arr))
