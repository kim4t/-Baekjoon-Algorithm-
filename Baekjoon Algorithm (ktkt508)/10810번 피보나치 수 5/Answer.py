n = int(input())
def fib(n):
    if(n<=2):
        return 1
    else:
        return fib(n-1)+fib(n-2)
if(n<2):print(n)
elif(n==2):print(1)
else:print(fib(n))