

def maxQuadrapulet(arr):
	arr.sort()

	return max(arr[-1]*arr[-2]*arr[-3]*arr[-4],arr[0]*arr[1]*arr[2]*arr[3],arr[-1]*arr[-2]*arr[0]*arr[1])


print(maxQuadrapulet([3,-1,3,2,-4,7,-5,-6]))