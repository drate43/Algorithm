from typing import List

def maxProfit(prices: List[int]) -> int:
    buyday = 0;
    sellday = 1;
    bestprofit = 0;
    while sellday < len(prices):
        profit = prices[sellday] - prices[buyday];
        if profit >= 0 :
            bestprofit = max(profit, bestprofit);
        else:
            buyday = sellday;
        sellday += 1;
    return bestprofit;



prices = [7,1,5,3,6,4];

value = maxProfit(prices);
print(value);
