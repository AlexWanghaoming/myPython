# 动态规划
# def uniquePaths(m, n):
#     if m == 1 or n ==1:
#         return 1
#     elif m == 2 and n ==2:
#         return 2
#     else:
#         return uniquePaths(m-1,n) + uniquePaths(m, n-1)

## 排列组合 代码实现 f函数代表x的阶乘
def uniquePaths(m, n):
    f = lambda x: f(x - 1) * x if x >= 2 else 1
    return int(f(m + n - 2) / (f(m - 1) * f(n - 1)))
if __name__ == '__main__':
    m = 7
    n = 3
    print(uniquePaths(m, n))