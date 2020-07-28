# leetcode 198
# def rob(nums):
#     """
#     动态规划算法每一个dp[len(nums)-1]是列表中的最后一个数代表偷到当前人家获利最多的偷法：
#     前提是至少隔一家偷
#     :param nums:
#     :return:
#     """
#     if len(nums)==0:
#         return 0
#     elif len(nums)<=2:
#         return max(nums)
#
#     dp=[nums[0], max(nums[0], nums[1])]
#
#     for i in range(2, len(nums)):
#         # print(i)
#         dp.append(max(dp[i-2]+nums[i], dp[i-1]))  # dp[i-1]代表偷到前一家为止获利最多方法可以获得的金额
#         # print(dp)
#     return dp[len(nums)-1]

def rob(nums):

    last = 0
    now = 0
    for i in nums:
        last, now = now, max(last + i, now)
        print(i)
        print("last:", last, "now:", now)
    return now


if __name__ == '__main__':
    nums = [2,1,1,2]
    print(rob(nums))