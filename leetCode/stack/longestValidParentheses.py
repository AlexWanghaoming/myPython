# leetcode 32
def longestValidParentheses1(s):
	if not s: return 0
	stack = [-1]
	l = 0
	for i in range(len(s)):
		if s[i] == "(":
			stack.append(i)
		else:
			stack.pop()
			if not stack:
				stack.append(i)
			else:
				l = max(l,i- stack[-1])    # 当前索引减去上一个栈中孤立括号的索引
	return l

# dp
# def longestValidParentheses2(s):
# 	if not s: return 0
# 	dp = [0]*len(s)   # dp 表示到i位置截止的最长有效括号
# 	for i in range(1,len(s)):
#


if __name__ == '__main__':
    s = "(()"
    print(longestValidParentheses1(s))