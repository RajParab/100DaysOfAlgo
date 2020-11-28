def revString(inputStr):
	words=inputStr.split(' ')
	ans=''
	for word in words:
		ans+=word[::-1]+' '
	return ans

print(revString('Raj Parab'))