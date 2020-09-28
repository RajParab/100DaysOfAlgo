#Question - https://leetcode.com/problems/online-stock-span

class StockSpanner:

    def __init__(self):
        self.stack=[]
        
    def next(self, price: int):
        self.ans=1
        
        if price==None:
            return price
        
        
        while self.stack and self.stack[-1][0]<=price:
            self.ans+=self.stack.pop()[1]
            
        self.stack.append([price,self.ans])
        
        
        
        return self.ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)