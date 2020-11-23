#Question - https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num=''
        while head:
            num+=str(head.val)
            head=head.next
            
        ans=int(num,2)
        return ans