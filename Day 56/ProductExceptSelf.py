

def products(nums):
	# Fill this in.
	ans=1
	result=[]
	for i in nums:
		ans*=i

	for i in nums:
		result.append(ans//i)
	return result

	
print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]