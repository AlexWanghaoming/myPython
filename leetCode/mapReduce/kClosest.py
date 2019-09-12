import math
def kClosest(points, K):
    a = lambda x: x[0] ** 2 + x[1] ** 2   # 可以单独定义lamda表达式
    points.sort(key=a)
    return points[:K]





if __name__ == '__main__':
    points = [[3,3],[5,-1],[-2,4]]
    K = 2
    print(kClosest(points, K))
