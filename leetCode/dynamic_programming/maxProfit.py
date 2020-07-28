# leetcode 121
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

# leetcode 122 动态规划算法
# 一维dp
# def maxProfit2(prices):
#     dp = [0] * len(prices)
#     for i in range(1, len(prices)):
#         if prices[i] - prices[i-1] + dp[i-1] > 0:
#             dp[i] = prices[i] - prices[i-1] + dp[i-1]
#         else:
#             dp[i] = 0
#     return max(dp)

## 解法2 用二维dp，分别表示天数和是否持有股票
def maxProfit2(prices):
    n = len(prices)
    dp = [[0]*2 for _ in range(n)]
    dp[0][0], dp[0][1] = 0, -prices[0]   # 第一天不买入和买入的收益分别是 0和-prices【0】
    for i in range(1,n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])     # 若当天不持有，可能的情况是前一天也不持有和当天刚卖出
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])     # 若当天持有，可能的情况是前一天持有或者前一天不持有当天买入
    return dp[n-1][0]

## leetcode 309
# 最佳买股票时机含冷冻期
# 方法一：三维dp分别表示 天数，是否持有股票和是否是冷冻期
def maxProfit3(prices):
    if not prices:
        return 0
    n = len(prices)
    dp = [[[0]*2 for _ in range(2)] for _ in range(n)]
    dp[0][0][0], dp[0][1][0], dp[0][0][1] = 0, -prices[0], 0
    for i in range(1,n):
        dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1])
        dp[i][1][0] = max(dp[i-1][0][0]-prices[i], dp[i-1][1][0])
        dp[i][0][1] = dp[i-1][1][0] + prices[i]
    return max(dp[n-1][0][0], dp[n-1][0][1])

# 方法二：二维dp分别表示天数和是否持有股票
# def maxProfit3(prices):
#     if not prices:
#         return 0
#     n = len(prices)
#     dp = [[0]*2 for _ in range(n)]
#     dp[0][0], dp[0][1] = 0, -prices[0]
#     for i in range(1,n):
#         dp[i][0] = max(dp[i-1][1]+prices[i], dp[i-1][0]) # 若当天不持有，分前一天持有当天卖出，前一天也不持有这两种情况
#         dp[i][1] = max(dp[i-2][0]-prices[i], dp[i-1][1]) # 若当天持有，1.分为前一天为冷冻期，大前天卖出，当天买入和 2前一天就持有这两种
#     return dp[n-1][0]

if __name__ == '__main__':
    # prices = [7,1,5,3,6,4]
    prices = [1,2,3,0,2]
    print(maxProfit3(prices))