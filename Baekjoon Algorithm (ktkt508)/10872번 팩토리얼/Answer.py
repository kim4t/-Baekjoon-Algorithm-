n = int(input())
def fec(n):
    if(n==1):
        return 1
    else:
        return n* fec(n-1)
if(n==0): print(1)
else: print(fec(n))


