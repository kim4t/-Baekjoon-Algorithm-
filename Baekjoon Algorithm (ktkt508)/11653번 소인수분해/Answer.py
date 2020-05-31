n = int(input())
a = 2
while a*a<=n:
    while n%a==0:
        n=n//a
        print(a)
    a+=1
if n>1:print(n)