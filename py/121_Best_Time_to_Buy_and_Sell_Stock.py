from typing import List


def maxProfit(prices: List[int]) -> int:
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


# unit test maxProfit
def test_maxProfit():
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert maxProfit([7, 6, 4, 3, 1]) == 0
    assert maxProfit([1, 2]) == 1
    assert maxProfit([3, 3]) == 0
    assert maxProfit([1, 2, 4]) == 3
