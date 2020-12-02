#Question - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3552/


class Solution:

    def __init__(self, head: ListNode):
        self.values=[]
        while head:
            self.values.append(head.val)
            head=head.next
        

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        import random
        return random.choice(self.values)