import sys
input = sys.stdin.readline
list = [1]*10001
s = int(len(list )*0.5)
for i in range(2,s+1):
    if(list[i]):
        for j in range(i+i,len(list),i):
            list[j] = 0

t = int(input())
for i in range(t):
    n = int(input())
    for j in range(n//2,1,-1):
        if(list[j] and list[n-j]):
            print(j,n-j)
            break