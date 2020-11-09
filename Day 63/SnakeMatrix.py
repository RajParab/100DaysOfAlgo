

def snakeMatrix(mat):
	row=len(mat)
	col=len(mat[0])
	ans=[]
	for i in range(row):
		if i%2==0:
			for j in range(col):
				ans.append(mat[i][j])
		else:
			j=col-1
			while j>=0:
				ans.append(mat[i][j])
				j-=1

	return ans

print(snakeMatrix([[1,2,3],[4,5,6],[7,8,9]]))