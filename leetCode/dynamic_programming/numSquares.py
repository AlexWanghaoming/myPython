# leetcode 279#

# 动态规划 超时
# def numSquares(n):
#     dp = [0]
#     for i in range(n):
#         dp.append(i+1)
#     for i in range(1, n+1):
#         if i>=4:
#             j = 1
#             while j*j <= i:
#                 dp[i] = min(dp[i], dp[i-j*j] + 1)
#                 j = j+1
#     return dp[-1]

# BFS   三要素： 队列容器（先进先出）、节点、已经访问的集合（避免重复访问）
from collections import deque
def numSquares(n):
    if n== 0:return 0
    que = deque([n])
    visit = []
    step = 0
    while que:
        step += 1
        l = len(que)
        for _ in range(l):
            tmp = que.pop()
            for i in range(1, int(tmp**0.5+1)):
                ss = tmp - i*i
                if ss == 0:
                    return step
                if not ss in visit:
                    visit.append(ss)
                    que.appendleft(ss)
if __name__ == '__main__':
    n = 7
    print(numSquares(n))