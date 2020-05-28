m = int(input())
n = int(input())
list = []
for i in range(m,n+1):
    num = i
    b= True
    if(num!=1):
        for j in range(2,num):
            if(num%j==0):
                b = False
                break
        if(b):
            list.append(num)
if(len(list)==0):
    print(-1)
else:
    sum = 0
    min = list[0]
    for i in list:
        if (i < min):
            min = i
        sum += i
    print(sum)
    print(min)


