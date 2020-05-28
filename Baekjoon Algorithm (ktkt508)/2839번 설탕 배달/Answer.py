n = int(input())
length1 = n//3
length2 = n//5
total = n
for i in range(length1+1):
    for j in range(length2+1):
        sum = 3*i + 5*j
        if(sum==n):
            t = i+j
            if(t<total):
              total =t
if(total==n):print(-1)
else: print(total)