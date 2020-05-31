a,b = map(int,input().split())
A = a
B = b
while(1):
    if(a%b==0):
        g= b
        break
    r = a%b
    a = b
    b = r
print(g)
A = A//g
B = B//g
print(g*A*B)