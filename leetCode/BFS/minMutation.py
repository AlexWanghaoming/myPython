from collections import deque
def minMutation(start, bank, end):
	bank = set(bank)
	if not end in bank:
		return -1
	queue=deque()
	queue.append((start,0))  # 初始化队列：基因序列和步数
	sub = {"A":"CGT","C":"AGT","T":"ACG","G":"ACT"}
	while queue:
		gene,step = queue.popleft()
		if gene == end:
			return step
		for idx,base in enumerate(gene):
			for i in sub[base]:
				curr = gene[:idx]+i+gene[idx+1:]   # 改变后的序列
				if curr in bank:
					queue.append((curr,step+1))
					bank.remove(curr)
	return -1

