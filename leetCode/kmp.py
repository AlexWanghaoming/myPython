"""
leetcode28 KMP 字符串匹配算法
参考阮一峰的网络日志
"""
import time

"""
写一个计算函数运行时间的装饰器
"""
def print_run_time(func):
    def wrapper(*args, **kw):
        local_time = time.time()
        func(*args, **kw)
        print('current Function [%s] run time is %.8f' % (func.__name__ ,time.time() - local_time))
    return wrapper


## 暴力解法
# @print_run_time
# def strStr(haystack: str, needle: str) -> int:
#     a = 0
#     b = 0
#     if needle == "":
#         return 0
#     while a < len(haystack) and b < len(needle):
#         if haystack[a] == needle[b]:
#             a = a+1
#             b = b+1
#             if b == len(needle):
#                 return a-b  # 返回首个位置
#         else:
#             a = a - b + 1  # haystack字符串 从 a-b+1 开始记
#             b = 0  # 模式串从头开始记
#     return -1

## kmp算法
# def strStr2(haystack: str, needle: str) -> int:





def partial_table(p):

    '''
    partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]
    建立部分匹配表
    '''

    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        # print(prefix, postfix)
        ret.append(len((prefix&postfix or {''}).pop()))   # 按位与逻辑运算符  这里集合中都是字符串 基本等同于集合求交集
    return ret


def kmp_match(s, p):

    m = len(s)
    n = len(p)
    cur = 0  #起始指针cur
    table = partial_table(p)
    while cur <= m-n:    # m-n 代表最多可以移动的位数
        for i in range(n):
            if s[i+cur] != p[i]:
                cur += max(i-table[i-1], 1) #有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                print(cur)
                break
        else:
            return True
    return False


if __name__ == '__main__':

    haystack = "hello"
    needle = "ll"
    # print(strStr(haystack, needle))

    print(partial_table("ABCDABD"))
    print(kmp_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))