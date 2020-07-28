
def findErrorNums(nums):
	l = len(nums)
	for i in range(l):
		if i+1 == nums[i]:
			continue
		else:
			return [nums[i], i+1]


if __name__ == '__main__':
    nums = [3,2,2]
    print(findErrorNums(nums))