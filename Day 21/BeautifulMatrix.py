#Question - https://codeforces.com/problemset/problem/263/A

for i in range(5):
    matrix=list(int(x) for x in input().split())
    pos=[]
    if 1 in matrix:
        pos=[i,matrix.index(1)]
        ans=abs(pos[0]-2)+abs(pos[1]-2)
        
    
print(ans)