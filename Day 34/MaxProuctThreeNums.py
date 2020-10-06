

def solution(nums):
	negArr=[]
	posArr=[]
	ans=[]
	for i in nums:
		if i<0:
			negArr.append(i)
		else:
			posArr.append(i)

	negArr.sort()
	posArr.sort()

	if len(negArr)>=2:
		ans.append(negArr[-1]*negArr[-2]*posArr[-1])

	if len(posArr)>2:
		ans.append(posArr[-1]*posArr[-2]*posArr[-3])

	return max(ans)

print(solution([-4,3,2,1,9,0]))