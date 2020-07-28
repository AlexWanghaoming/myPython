
def orangesRotting(grid):
	from collections import deque
	que = deque()
	m = len(grid)
	n = len(grid[0])
	for i in range(m):
		for j in range(n):
			if grid[i][j] == 1:
				que.append((i,j))
	t = 0
	while que:   # BFS
		rm = []
		t += 1
		l = len(que)
		for i in range(l):
			x,y = que[i]
			if (x+1<m and grid[x+1][y] == 2) or (x>0 and grid[x-1][y] == 2) or (y+1<n and grid[x][y+1] == 2) or (y>0 and grid[x][y-1] == 2):
				rm.append((x,y))
		for i in rm:
			grid[i[0]][i[1]] = 2
			que.remove(i)
		if not rm:
			return -1
	return t
if __name__ == '__main__':
    g = [[2,1,1],[1,1,0],[0,1,1]]
    print(orangesRotting(g))