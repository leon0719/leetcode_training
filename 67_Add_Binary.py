def addBinary(a: str, b: str) -> str:
    return str(bin(int("0b"+a,2) + int("0b"+b,2))[2:])




if __name__ == "__main__":
    a = "1010"
    b = '1011'

    print(addBinary(a, b))