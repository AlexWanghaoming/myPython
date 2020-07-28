
# 二维动态规划 leetcode 221
def maximalSquare(matrix):
    nrow = len(matrix)
    ncol = len(matrix[0])

    dp = [[0] * ncol for  _ in range(nrow)]    # dp 表示以此位置为右下角的正方形的最大面积

    area = 0
    for i in range(nrow):
        for j in range(ncol):
            if i == "0" or j == "0":
                dp[i][j] = matrix[i][j]

            else:
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    area = max(area,dp[i][j])
                else:
                    dp[i][j] = 0
    return area*area


if __name__ == '__main__':
    matrix = [[1,0,1,0,0],
              [1,0,1,1,1],
              [1,1,1,1,1],
              [1,0,0,1,0]]
    matrix = [list(map(str, i)) for i in matrix]
    print(maximalSquare(matrix))


