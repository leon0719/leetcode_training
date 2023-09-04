"""
目標是找到一個加油站的起點，使你可以繞著一個圓形公路行駛，而不會耗盡汽油。
你需要計算每個加油站的汽油餘量，如果在某個加油站汽油餘量變為負數，
則將起點移動到下一個加油站，
最終返回一個有效的起點或-1(如果無法找到合適的起點)。這個問題可以使用貪婪算法來解決。

1. 首先，它檢查總加油量是否小於總花費，如果是，則直接返回-1，因為這表示無法完成整個旅程。
2. 接下來，進入一個 for 迴圈，遍歷每個加油站的索引 i。
3. 在每個迴圈中，計算當前加油站的汽油餘量（gas[i]）減去到達下一個加油站所需的汽油量（cost[i]），並將結果存儲在 total 變數中
4. 如果在某個加油站 i，total 變為負數，這意味著無法從當前加油站出發前進到下一個加油站
5. 因此需要重新選擇起點。在這種情況下，它將 start 設置為下一個加油站的索引 i + 1，並將 total 重置為0，以重新開始計算
6. 最終，當 for 迴圈遍歷完所有加油站後，如果成功找到了一個合適的起點（能夠繞行整個圓形公路），則返回 start，否則返回-1
"""

from typing import List


def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    station_index = 0
    total = 0
    for index, _ in enumerate(gas):
        total += gas[index] - cost[index]
        if total < 0:
            station_index += 1
            total = 0
    return station_index


# Unit Test Code
def test_canCompleteCircuit():
    assert canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3


def test_canCompleteCircuit_2():
    assert canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
