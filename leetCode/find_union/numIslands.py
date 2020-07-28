## leetcode 200

# 并查集
def numIslands1(grid):
	f = {}

	def find(x):  # 递归
		f.setdefault(x,x)
		if f[x] != x:
			f[x] = find(f[x])
		return f[x]

	def union(x,y):
		f[find(x)] = find(y)

	if not grid: return 0

	row = len(grid)
	col = len(grid[0])

	for i in range(row):
		for j in range(col):
			if grid[i][j] == 1:
				for x,y in [[-1,0], [0,-1]]:
					tmp_i = x+i
					tmp_j = y+j
					if 0<=tmp_i<row and 0<=tmp_j<col and grid[tmp_i][tmp_j] == 1:
						union(tmp_i*col+tmp_j, i*col+j)
	res = set()
	for i in range(row):
		for j in range(col):
			if grid[i][j] == 1:
				res.add(find(i*col+j))
	return len(res)

# BFS
from collections import deque
def numIslands2(grid):
	if grid == [] or grid == [[]]: return 0
	m,n = len(grid), len(grid[0])
	visited = [[False] * n for _ in range(m)]
	print(visited)
	num = 0
	directions = [[0,1], [1,0], [0,-1], [-1,0]]
	for i in range(m):
		for j in range(n):
			if not visited[i][j] and grid[i][j] == 1:
				## bfs
				que = deque()
				que.append([i,j])
				visited[i][j] = True
				while len(que) > 0:
					a,b = que.popleft()
					for d in directions:
						new_a = d[0]+a
						new_b = d[1]+b
						if 0<=new_a<m and 0<=new_b<n and grid[new_a][new_b] == 1 and not visited[new_a][new_b]:
							que.append([new_a, new_b])
							visited[new_a][new_b] = True
				num += 1
	return num

# DFS 递归
def numIslands3(grid):
	def dfs(i, j):
		visited[i][j] = True
		for d in directions:
			new_i = i + d[0]
			new_j = j + d[1]
			if 0 <= new_i < m and 0 <= new_j < n and not visited[new_i][new_j] and grid[new_i][new_j] == 1:
				dfs(new_i, new_j)

	m,n = len(grid), len(grid[0])
	visited = [[False]*n for _ in range(m)]
	directions = [[0,1], [1,0], [-1,0], [0,-1]]
	num = 0
	for i in range(m):
		for j in range(n):
			if not visited[i][j] and grid[i][j] == 1:
				# DFS
				dfs(i,j)
				num+=1
	return num


if __name__ == '__main__':
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]
    print(numIslands3(grid))