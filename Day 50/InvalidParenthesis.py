def count_invalid_parenthesis(string):
	ans=[string[0]]
	void=[]
	for i in string[1:]:
		if i=='(':
			ans.append(i)
		elif i==')' and (len(ans)==0 or ans[-1]!='('):
			void.append(i)
		elif i==')' and ans[-1]=='(':
			ans.pop()

	return len(ans)+len(void)


print(count_invalid_parenthesis(")("))
# 1