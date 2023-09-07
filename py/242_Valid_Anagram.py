def isAnagram(s: str, t: str) -> bool:
    s = sorted([i for i in s])
    t = sorted([i for i in t])
    return s == t


if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))
