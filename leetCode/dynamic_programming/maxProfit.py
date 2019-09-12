# def maxProfit(prices):
#     # l = []
#     if not prices:
#         return 0
#     min_price = prices[0]
#     max_profit = 0
#     for i in range(1, len(prices)):
#         if prices[i] < min_price:
#             min_price = prices[i]
#         if prices[i] - min_price > max_profit:
#             max_profit = prices[i] - min_price
#     return max_profit

# 动态规划算法
# 思路：维护两个变量，一个是到目前为止最好的交易，另一个是在当天卖出的最佳交易(dp)（也就是局部最优）。其实，就是求一个数组中连续子数组差最大
def maxProfit(prices):
    dp = [0] * len(prices)
    for i in range(1, len(prices)):
        if prices[i] - prices[i-1] + dp[i-1] > 0:
            dp[i] = prices[i] - prices[i-1] + dp[i-1]
        else:
            dp[i] = 0
    return max(dp)


if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))