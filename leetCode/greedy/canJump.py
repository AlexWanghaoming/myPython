# def canJump(nums: list) -> bool:
#     if nums.count(0) == 0 or all(n == 0 for n in nums):
#         return True
#     if nums.index(0) + 1 == len(nums):
#         return True
#     zero_idx = [i for i, x in enumerate(nums) if x == 0]
#     for idx, j in enumerate(nums):
#         # if j == 0:
#         #     break
#         if all(n >= idx + j for n in zero_idx):
#             print(idx + j)
#             continue
#         else:
#             return True
#     return False


def canJump2(nums: list) -> bool:
    start = 0
    end = 0
    n = len(nums)
    while start <= end and end < len(nums) - 1:
        end = max(end, nums[start] + start)   # end 表示从start位点开始最远可能到达的位置
        start += 1
        print(start, end)
    return end >= n - 1


if __name__ == '__main__':
    nums = [3, 2, 1, 0, 4]
    print(canJump2(nums))