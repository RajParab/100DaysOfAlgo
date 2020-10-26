def inRange(grid, r, c):
	numRow, numCol = len(grid), len(grid[0])
	if r < 0 or c < 0 or r >= numRow or c >= numCol:
	  return False
	return True

def numIslands(grid):
	count=0
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j]==1:
				if inRange(grid,i+1,j) and grid[i+1][j]==1:
					count+=1
				elif inRange(grid,i,j+1) and grid[i][j+1]==1:
					count+=1
				
	return count

grid = [[1, 0, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0]]
print(numIslands(grid))