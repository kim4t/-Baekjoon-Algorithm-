t = int(input())
list = []
for i in range(t):
    list.append(int(input()))
n = abs(list[1]-list[0])
num = []
num.append(n)
for i in range(2,int(n**0.5)+1):
    if(n%i==0):
        num.append(i)
        if(i!=n//i):
            num.append(n//i)
num.sort()
for i in num:
    mod = list[0]%i
    same = True
    for j in range(len(list)):
        if(list[j]%i!=mod):
            same = False
            break
    if(same):
        print(i,end=' ')

