
# 斐波那契数列
## [1,1,2,3,5,8,13,21]
## f(n) = f(n-1) + f(n-2)
def climbStairs(n):
    d = [1,1]
    for i in range(2,n+1):
        d.append(d[i-1] + d[i-2])
    return d[-1]

if __name__ == '__main__':
    n = 5
    print(climbStairs(n))