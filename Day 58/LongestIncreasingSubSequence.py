#LongestIncreasingSubSequence

def LongestIncreasingSubSequence(arr):
	ans=[1]*len(arr)

	for j in range(1, len(arr)):
		for i in range(j):
			if arr[j]>=arr[i]:
				ans[j]=max(ans[i]+1, ans[j])


	return max(ans)

print(LongestIncreasingSubSequence([-1,3,4,5,2,2,2,2]))
