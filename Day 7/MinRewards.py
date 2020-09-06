
#Naive Approach -> time - O(N^2), space - O(N)
def minReward(scores):
	"""
	-Get an array with initialized value 1 of length same as scores
	-If previous value is less than this one increment the reward by 1
	-If previous value is greater than current score initialize the current reward to 1 
	 and increment all the previous value by one.
	-Get the sum of all the values in reward array for the final answer

	"""
	reward=[1 for _ in range(len(scores))]
	prev=scores[0]
	answer=0
	count=0
	for i in range(1,len(scores)):
		if scores[i]>prev:
			reward[i]=max(reward[i],reward[i-1]+1)
			count=i
		if scores[i]<prev:
			#reward[i]=1
			for j in reversed(range(count,i)):

				reward[j]=max(reward[j],reward[j+1]+1)

		#print(scores,'\n',reward,prev,count)
		prev=scores[i]
		
	for i in reward:
		answer+=i

	return answer

#print(minReward([8,4,2,1,3,6,7,9,5]))

#Optimum Approach -> time - O(N), space- O(N)
def minRewards(scores):
	"""
	-Get all the local minimums in the entire array 
	-Add up values by 1 to both sides of the local minimum till the trend continues

	"""
	reward=[1 for _ in range(len(scores))]

	localMin=[]
	if scores[0]<scores[1]:
		localMin.append(0)
	for i in range(1,len(scores)-1):
		if scores[i]<scores[i+1] and scores[i]<scores[i-1]:
			localMin.append(i)
	if scores[-1]<scores[-2]:
		localMin.append(len(scores)-1)
	

	for i in localMin:
		#Check right of the local minimum till the numbers are increasing
		currentMin=i+1
		while(currentMin<len(scores) and scores[currentMin]>scores[currentMin-1]):
			reward[currentMin]=max(reward[currentMin],reward[currentMin-1]+1)
			currentMin+=1

		#Check left of the local minimum till the numbers are increasing
		currentMin=i-1
		while(currentMin>=0 and scores[currentMin]>scores[currentMin+1]):
			reward[currentMin]=max(reward[currentMin],reward[currentMin+1]+1)
			currentMin-=1

	answer=0
	for i in reward:
		answer+=i

	return answer


print(minRewards([0,8,4,2,1,3,6,7,9,5,6,0,7]))