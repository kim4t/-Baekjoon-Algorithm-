m,n = map(int,input().split())
n = n+1
list = [True]*n
s = int(n**0.5)
for i in range(2,s+1):
    if(list[i]):
        for j in range(i+i,len(list),i):
            list[j]=False
for i in range(m,n):
    if(i>1 and list[i]):
        print(i)
