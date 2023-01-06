from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    if strs == [] or len(strs) == 1:
        return None
    else:
        strs.sort()
        prefix = ""
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                prefix += strs[0][i]
            else:
                break
    return prefix


if __name__ == "__main__":
    test = ["fliwer", "fliw", "flight"]
    print(longestCommonPrefix(test))
