# leetcode 213
def rob(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) <=2:
        return max(nums)
    else:
        # 坚决不抢第一个，可以抢最后一个
        dp1 = [0, nums[1]]
        for i in range(2, len(nums)):
            dp1.append(max(dp1[i-2]+nums[i], dp1[i-1]))
        # 坚决不抢最后一个， 第一个可以抢
        dp2 = [nums[0], max(nums[0], nums[1])]
        for j in range(2, len(nums)-1):
            dp2.append(max(dp2[j-2]+nums[j], dp2[j-1]))

        return max(dp1[len(nums)-1], dp2[len(nums)-2])  # 两种情况取较大值
if __name__ == '__main__':
    nums = [3,2,3]
    print(rob(nums))