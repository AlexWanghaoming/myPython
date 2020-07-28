def maxDistance(grid):  # 要找距离陆地最远的海洋，就先对所有陆地BFS
	"""
	:type grid: List[List[int]]
	:rtype: int
	"""
	from collections import deque
	n = len(grid)
	queue = deque()
	dx = [1, -1, 0, 0]
	dy = [0, 0, 1, -1]
	for i in range(n):
		for j in range(n):
			if grid[i][j] == 1:  # 先找所有的陆地
				queue.append((i, j))
	if len(queue) == 0 or len(queue) == n * n:  # 全为海洋或全为陆地
		return -1
	distance = -1  # 为啥是-1呢，因为第一次BFS是所有的陆地，第二次BFS才开始海洋，-1保证在第二次搜索时距离为1
	while queue:
		l = len(queue)
		for _ in range(l):
			cur = queue.popleft()
			x0, y0 = cur
			for k in range(4):
				x = x0 + dx[k]
				y = y0 + dy[k]

				if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:  # 找到海洋了
					grid[x][y] = 1
					queue.append((x, y))
		distance += 1
	return distance