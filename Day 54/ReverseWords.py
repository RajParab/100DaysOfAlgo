

class Solution:
	def reverseWords(self, string):
		ans=''
		arr=string.split(' ')
		for word in arr:
			ans+=word[::-1]+' '

		return ans

print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah