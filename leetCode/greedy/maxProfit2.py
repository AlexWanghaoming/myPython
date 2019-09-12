def maxProfit(prices):
    """
    贪心算法
    寻找利润最大卖出的日子其实和买入在价格升高时直接卖掉然后再在当天买入获得的利润相同
    :param prices:
    :return: profit
    """
    profit = 0
    for i in range(1,len(prices)):
        profit += max(0, prices[i] - prices[i-1])
        print(profit)
    return profit


if __name__ == '__main__':

    prices = [1,2,3,4,5]
    print(maxProfit(prices))




