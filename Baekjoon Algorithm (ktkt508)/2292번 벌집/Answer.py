n = int(input())
list = []
p = 0
for i in range(1, n+1):
    a = 2+(3*i*(i-1))
    if(a>n):
        p = i
        break
print(p)
