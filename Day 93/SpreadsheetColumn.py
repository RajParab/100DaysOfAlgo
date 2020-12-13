class Solution:
	def convertToTitle(self, n):
    	# Fill this in.
		letter={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',
				9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',
				17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',0:'Z'}
		
		mod=[]
		while(n>0):
			print(mod)
			if n==26:
				mod.append(0)
				n-=26
			else:
				mod.append(n%26)
				n=n//26

		mod=mod[::-1]
		ans=''
		for i in mod:
			ans+=letter[i]
		return ans


input1 = 1
input2 = 456976
input3 = 28
print(Solution().convertToTitle(input1))
# A
print(Solution().convertToTitle(input2))
# YYYZ
print(Solution().convertToTitle(input3))
# AB