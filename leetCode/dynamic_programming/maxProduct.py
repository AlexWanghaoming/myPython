#   leetcode 152
def maxProduct(nums):
	res = nums[0]
	ma = nums[0]
	mi = nums[0]
	for i in nums[1:]:
		cur_max = max(i*mi, i*ma, i)
		cur_min = min(i*mi, i*ma, i)
		res = max(res, cur_max)
		ma = cur_max
		mi = cur_min
	return res





if __name__ == '__main__':
    nums = [-1,-2,-9,-6]
    print(maxProduct(nums))
