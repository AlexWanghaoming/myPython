
# leetcode 392 双指针思想, 判断是否含有子字符串用while循环：O(n)

def isSubsequence(s: str, t: str) -> bool:
    len_s = len(s)
    len_t = len(t)
    i = 0
    j = 0
    while(i < len_s and j < len_t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == len_s:
        return True
    else:
        return False
