n = int(input())
total = 0
f = n
while (True):
    a = n//10
    b = n%10
    c = a+b
    if(c>=10):
        c = c%10
    n = (b*10)+c
    total += 1
    if f == n:break
print(total)