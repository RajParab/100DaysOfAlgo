"""
GCD is Greatest Common Divisor

Two Ways of getting GCD are mentioned below

"""



def recursiveGCD(a,b):
	"""
	Recursive method we find the mod of the bigger number till one of the two is zero
	"""
	if a==0:
		return b
	else:
		if a>b:
			gcd=recursiveGCD(a%b,b)
		else:
			gcd=recursiveGCD(b%a,a)

	return gcd


#print(recursiveGCD(21,7))


def bitwiseGCD(a,b):
	"""
	In Binary Method we make both the numbers odd and subtract the bigger number wuth smaller till one of them is zero

	a & 1 is similiar to a % 2
	a >> 1 is similiar to a / 2
	a << 1 is similiar to a * 2 
	"""
	if a==0 or a==b:
		return b
	elif b==0:
		return a

	while (a&1 == 0 and b&1==0):
		a=a>>1
		b=b>>1

	while(a&1==1 and b&1==0):
		b=b>>1

	while(a&1==0 and b&1==0):
		a=a>>1

	if a>b:
		return bitwiseGCD(a-b,b)
	else:
		return bitwiseGCD(a,b-a)


#print(bitwiseGCD(15,30))