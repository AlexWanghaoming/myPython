# leetcode 486 预测赢家 二维动态规划


def PredictTheWinner(nums):
    L = len(nums)
    if L%2 == 0 or L == 1:  # 如果有偶数张，玩家1必赢
        return True

    dp = [[0] * L for _ in range(L)]    # dp 代表从[i,j]子结构的最优情况下的玩家1净胜分数, 填充方向是从下往上，从左往右
    for i in range(L-1, -1, -1):
        for j in range(i, L):
            if i == j:
                dp[i][j] = nums[i]
            elif j-i == 1:
                dp[i][j] = abs(nums[i] - nums[j])
            else:
    # 对于j-i > 1的情况，如果玩家1先手拿了num[i]玩家2一定会拿[i+1,j]中的最佳拿法即dp[i+1][j]；如果玩家一先手拿了nums[j]同理
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])

    if dp[0][L-1] >= 0:
        return True
    else:
        return False
if __name__ == '__main__':
    nums = [1, 5, 2]
    print(PredictTheWinner(nums))