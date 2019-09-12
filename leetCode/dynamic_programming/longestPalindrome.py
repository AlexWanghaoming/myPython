# leetcode5 马拉车算法，O(n)； 动态规划： O(n^2)

# def longestPalindrome(s: str) -> str:
#     """
#     dp 不用考虑s的奇偶性，较普适
#     """
#
#     size = len(s)
#     if size <= 1
#         return s
#
#     dp = [[False for _ in range(size)] for _ in range(size)] # 二维dp初始化
#     longest = 1
#     res = s[0]
#
#     for r in range(1, size):   # 遍历所有字串情况  r代表右边索引；i代表左边索引
#         for i in range(r):
#             if s[i] == s[r] and (r-i <= 2 or dp[i+1][r-1]):
#                 dp[i][r] = True    # dp状态方程
#                 cur_len = r - i + 1  # 当前字串长度
#                 if cur_len > longest:     #  更新最长回文字串
#                     longest = cur_len
#                     res = s[i:r + 1]
#     # # 调试语句
#     # for item in dp:
#     #     print(item)
#     # print('---')
#     return  res


def longestPalindrome(s):

    """
    马拉车算法 O(n)
    center: 回文字串的中心位置
    mx：回文字串的最后位置
    """
    if len(s) <= 1:
        return s
    ss = "^#" + "#".join(s) + "#$"   # 首位分别加^,$ 防溢出   ss = 2 * len（s） + 1 必为奇数
    mx = 0
    center = 0
    max_str = ""
    p = [0]*len(ss)     # p[i] 表示以ss[i]为中心的最长回文字串的半径（不包括p[i]本身）

    for i in range(1, len(p) - 1):

        if i < mx:
            j = 2*center - i   # j 是i 关于 mx 关于 id 的对称点
            p[i] = min(mx - i, p[j])   # Manacher 算法的精髓

        # 尝试继续向两边扩展，更新 p[i]
        while ss[i - p[i] - 1] == ss[i + p[i] + 1]:  # 继续中心拓展法 不必判断是否溢出，因为首位均有特殊字符，肯定会退出
            p[i] += 1

        # 更新中心
        if i + p[i] > mx:
            mx = i + p[i]
            center = i

        # 更新最长串
        if 1 + 2 * p[i] > len(max_str):
            max_str = ss[i - p[i]: i + p[i] + 1]

    return max_str.replace('#', '')








if __name__ == '__main__':
    print(longestPalindrome("cbbdbba"))