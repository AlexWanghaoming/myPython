## 蒙特卡洛算法求圆周率
import random

def monteCarlo(n):
    count = 0
    for _ in range(n):
        x = random.uniform(0, 2)
        y = random.uniform(0, 2)
        if x*x + y*y < 4:  # 圆的标准方程求
            count += 1
    return count/n * 4


if __name__ == '__main__':
    print(monteCarlo(10000))