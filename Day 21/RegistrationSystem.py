#Question - https://codeforces.com/problemset/problem/4/C

n=int(input())
a_dict={}
for i in range(n):
    a=input()
    if a not in a_dict:
        a_dict[a]=1
        print('OK')
    elif a in a_dict:
        a_dict[a]+=1
        print("%s%d"  %(a,a_dict[a]-1))