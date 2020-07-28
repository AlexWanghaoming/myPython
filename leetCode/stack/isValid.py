# leetcode 20

def isValid(s):
	dic = {")":"(",
	       "]":"[",
	       "}":"{"}
	stack = []
	for i in s:
		if i not in dic:
			stack.append(i)
		else:
			if len(stack) == 0:
				return False
			elif stack.pop() == dic[i]:
				continue
			else:
				return False
	return len(stack) == 0




if __name__ == '__main__':
    s = "()[]{())}"
    print(isValid(s))
