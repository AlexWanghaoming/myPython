class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        lookup = {}
        for i in range(n):
            tmp = target - nums[i]
            if tmp in lookup:
                return [lookup[tmp], i]
            lookup[nums[i]] = i


if __name__ == "__main__":
    ll = [3,2,4]
    tt = 6
    ss = Solution()
    print(ss.twoSum(ll,tt))
