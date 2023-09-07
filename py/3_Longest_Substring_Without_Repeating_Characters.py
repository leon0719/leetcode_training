def length_of_longest_substring(s):
    v = set()
    maxNum = 0
    start, end = 0, 0
    while end < len(s):
        if s[end] not in v:
            v.add(s[end])
            end += 1
            maxNum = max(maxNum, end - start)
        else:
            v.remove(s[start])
            start += 1
    return maxNum


if __name__ == "__main__":
    s = "abcabcbb"
    print(length_of_longest_substring(s))
