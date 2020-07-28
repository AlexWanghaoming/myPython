# leetcode 120

def minimumTotal(triangle):
	n = len(triangle)
	dp = [[0]*i for i in map(len, triangle)]
	dp[0][0] = triangle[0][0]
	for i in range(1,n):
		dp[i][0] = dp[i-1][0] + triangle[i][0]
		dp[i][-1] = dp[i-1][-1] + triangle[i][-1]
	for i in range(2,n):
		k = i+1  # 当前行元素个数
		for j in range(1,k-1):
			dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + triangle[i][j]

	return min(dp[-1])


if __name__ == '__main__':
	triangle = [[2], [3,4], [6,5,7], [4,1,8,3]]
	print(minimumTotal(triangle))

