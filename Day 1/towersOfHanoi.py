


def towersOfHanoi(n,start,using,to):
	
	if n==1:
		print('Move disk from',start,'to',to)
		return
	
	towersOfHanoi(n-1,start,to,using)
	print('Move disk from',start,'to',to)
	towersOfHanoi(n-1,using,to,start)
	


towersOfHanoi(3,'A','B','C')