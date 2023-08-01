from typing import List

"""
該函式使用一個迴圈來遍歷prices列表中的元素。在每次迴圈中，
它比較當前價格（prices[i]）與前一個價格（prices[i - 
如果當前價格大於前一個價格，則表示可以在前一天購買股票，然後在當天賣出，這樣就可以獲得利潤


"""


def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]

    return max_profit


# test


print(maxProfit([7, 1, 5, 3, 6, 4]))
