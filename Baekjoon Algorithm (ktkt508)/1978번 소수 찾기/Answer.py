import math
n = int(input())
l = input().split()
count = 0
for i in range(n):
    a = int(l[i])
    s = math.sqrt(a)
    s = int(s//1)
    b = True
    if(a!=1):
        for j in range(2, s+1):
            if (a % j == 0):
                b = False
                break
        if (b):
            count += 1

print(count)

