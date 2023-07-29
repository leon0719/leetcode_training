def climbStairs(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    result = 0
    pre = 1
    next = 2
    for _ in range(2, n):
        result = pre + next
        pre = next
        next = result
    return result


if __name__ == "__main__":
    out = climbStairs(4)
    print(out)
