

def runningMedian(arr):
	ans=[]
	for i in range(len(arr)):
		s=arr[:i+1]
		s.sort()
		if len(s)%2==1:
			ans.append(s[i//2])
		else:
			ans.append((s[i//2]+s[(i//2)+1])/2)

	return ans

print(runningMedian([2, 1, 4, 7, 2, 0, 5]))