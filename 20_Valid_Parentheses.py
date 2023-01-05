def is_valid(s: str) -> bool:
    stack = []
    mapping = {'(': ')', '[': ']', '{': '}'}
    for c in s:
        if c in mapping:
            stack.append(c)
        elif not stack or mapping[stack.pop()] != c:
            return False
    return not stack





if __name__ == '__main__':
    s = '{[()]}'
    print(is_valid(s))