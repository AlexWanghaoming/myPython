#动态规划算法
def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)  # 首先将dp中的所有值赋值为inf，无限大
    print(dp)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            # dp[i]表示金额为i需要最少的金额是多少,
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)  # dp 方程
                print(dp[i])
    return dp[-1] if dp[-1] != float('inf') else -1

if __name__ == '__main__':
    coins = [1,2,5]
    amount = 11

    print(coinChange(coins, amount))