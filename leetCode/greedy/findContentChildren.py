# def findContentChildren(appetite, size):
#     appetite = sorted(appetite, reverse=True)
#     size = sorted(size, reverse=True)
#     l1 = len(appetite)
#     for i in range(l1):
#         if all(appetite[i] > j for j in size) :
#             l1 = l1 -1
#         else:
#             size.pop(0)
#     return l1

def findContentChildren(g, s):
    """
    :param g:
    :param s:
    :return:
    先对 g,s 从小到大排序贪心算法希望最小的饼干可以满足胃口最小的孩子,否则用第二小的饼干取尝试满足胃口最小的孩子


    """
    g.sort()
    s.sort()
    g_len = len(g)
    s_len = len(s)
    i = 0
    j = 0

    while(i < g_len and j < s_len):
        if g[i] <= s[j]:
            i = i + 1
            j = j + 1
        else:
            j = j + 1
    return i

if __name__ == "__main__":
    g = [1,2,6,7]
    s = [1,2,3,4,11]
    print(findContentChildren(g, s))


