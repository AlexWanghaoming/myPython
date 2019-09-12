# 编辑距离 递归解法
def minDistance(s1, s2):

    def dp(i, j):
        # base case
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1

        if s1[i] == s2[j]:
            return dp(i-1, j-1)
        else:
            return min(dp(i, j-1) + 1,  # 插入
                       dp(i-1, j) + 1,  # 删除
                       dp(i-1, j-1) + 1)  # 替换
    return dp(len(s1) - 1, len(s2) - 1)   ## dp 初始化指向最后一个索引


if __name__ == '__main__':
    s1 = "horse"
    s2 = "ros"
    print(minDistance(s1, s2))