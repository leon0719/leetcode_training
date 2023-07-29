from typing import List


def Pascal_triangle(numRows: int) -> List[List[int]]:
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    else:
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            temp = [1]
            for j in range(1, i):
                temp.append(result[i - 1][j - 1] + result[i - 1][j])
            temp.append(1)
            result.append(temp)
        return result


# unit test Pascal_triangle


def test_Pascal_triangle():
    assert Pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert Pascal_triangle(1) == [[1]]
    assert Pascal_triangle(0) == []
    assert Pascal_triangle(2) == [[1], [1, 1]]
    assert Pascal_triangle(3) == [[1], [1, 1], [1, 2, 1]]
    assert Pascal_triangle(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert Pascal_triangle(6) == [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
    ]
