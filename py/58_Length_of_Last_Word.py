def lengthOfLastWord(s: str) -> int:
    return len("".join(s.rstrip().split(" ")[-1]))


if __name__ == "__main__":
    test = "hello world  "
    print(lengthOfLastWord(test))
