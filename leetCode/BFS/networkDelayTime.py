from collections import deque

def networkDelayTime1(times,N, K):
	node = [i for i in range(1,N+1)]
	q = deque()
	q.append((K,0))
	while q:
		n,t = q.popleft()
		for u,v,w in times:
			if u == n:
				q.append((v,t+w))
	print(node)
	print(q)
				# node.remove(v)
		# q = sorted(q, key=lambda x:x[1],reverse=True)


# 优先级队列
import collections
import queue

def networkDelayTime2(times, N: int, K: int) -> int:
	graph = collections.defaultdict(list)  # 将图变成{u:[(v,w)]}
	for item in times:
		graph[item[0]].append((item[1], item[2]))

	q = queue.PriorityQueue()  # 优先级队列每次抽取出时间最短的节点
	q.put((0, K))
	time_list = [float('inf')] * N  # 记录每个节点的时间
	time_list[K - 1] = 0
	visited = {}  # 记录到达每个节点所耗费时间

	while not q.empty():
		node = q.get()
		visited[node[1]] = node[0]

		# 可能这个节点没有指向别的节点，也就没被写入graph
		if node[1] in graph:
			for item in graph[node[1]]:
				# 如果已经出现在visted就说明已经找到最短路径
				# 可以不写这个if，正确性不影响，
				# 但是写可以节约一些没必要的遍历
				if item[0] not in visited:
					temp = item[1] + node[0]
					# 如果此时的时间比上一次遍历到的更短，就刷新
					if temp < time_list[item[0] - 1]:
						q.put((temp, item[0]))
						time_list[item[0] - 1] = temp
	return -1 if len(visited) != N else max(time_list)

if __name__ == '__main__':
	times = [[1,2,1], [2,3,2], [1,3,4]]
	N = 3
	K = 1
	print(networkDelayTime2(times, N,K))