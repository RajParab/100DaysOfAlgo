

def result(a):
	element=[]
	while(a!=1):
		print(a)
		for i in range(9,1,-1):
			if a%i==0:
				a/=i
				element.append(i)
				#break
	element.sort()
	return element

print(result(150))