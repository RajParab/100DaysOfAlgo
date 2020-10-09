#Questions - https://leetcode.com/problems/merge-k-sorted-lists



class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists)==0 or set(lists)=={None}:
            return None
        
        curr=ListNode(0)
        head=curr
        item=[]
        for i in range(len(lists)):
            while(lists[i]):
                item.append(lists[i].val)
                lists[i]=lists[i].next
        print(item)
        item.sort()
        for x in item:
            curr.next=ListNode(x)
            curr=curr.next
            
            
        
        return head.next