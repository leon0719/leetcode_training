from typing import List

def plusOne(digits: List[int]) -> List[int]:
    return [int(i) for i in str(int(''.join(str(dig) for dig in digits))+1)]




if __name__ == "__main__":
    test =[9]
    print(plusOne(test))

