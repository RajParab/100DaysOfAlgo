#Question - https://leetcode.com/problems/merge-in-between-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        count=1
        start_list2=list2
        import copy
        ans=copy.deepcopy(list1)
        result=ans
        while list2.next is not None:
            list2=list2.next
            
        end_list2=list2
        
        while count<a:
            count+=1
            ans=ans.next
            list1=list1.next
        ans.next=start_list2
        list1=list1.next
        count+=1
        
        while count<=b:
            count+=1
            list1=list1.next
        print(list1)
        end_list2.next=list1.next
        
        return result
    