# leetcode 53 最大子序和

def maxSubArray(nums):
	n = len(nums)
	dp = [0]*n   # 定义dp数组为以nums[i]结尾的最大子序和
	dp[0] = nums[0]
	for i in range(1,n):
		dp[i] = max(dp[i-1]+nums[i], nums[i])
	return max(dp)

if __name__ == '__main__':
	nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
	print(maxSubArray(nums))