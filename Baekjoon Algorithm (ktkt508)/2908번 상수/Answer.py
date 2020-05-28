a,b = input().split()
n1=''
n2=''
for i in range(2,-1,-1):
    n1+=a[i]
    n2+=b[i]
if(n1>n2): print(n1)
else: print(n2)