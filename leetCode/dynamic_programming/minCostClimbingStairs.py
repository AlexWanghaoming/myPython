def minCostClimbingStairs(cost):

    p1, p2 = 0, 0   # p1 代表当前台阶的前一个台阶，p2 代表当前台阶的前两个，初始都是0
    for i in range(2, len(cost) + 1):
        p1, p2 = p2, min(p2 + cost[i-1], p1 + cost[i-2])
    print(p2)


if __name__ == '__main__':
    cost = [1,1,2,3,1,2,3]
    minCostClimbingStairs(cost)
