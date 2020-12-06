#Question - https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/569/week-1-december-1st-december-7th/3556/


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        def bfs(node):
            queue = deque()
            queue.append(node)
            output = []
            
            while queue:
                size = len(queue)
                curr = []
                for i in range(size):
                    popped = queue.popleft()
                    curr.append(popped)
                    if popped.left:
                        queue.append(popped.left)
                    if popped.right:
                        queue.append(popped.right)
                output.append(curr)
            return output
        output = bfs(root)
        # Shift the pointers
        for level in output:
            for i in range(len(level)-1):
                level[i].next = level[i+1]
            level[-1].next = None

        
        return output[0][0]