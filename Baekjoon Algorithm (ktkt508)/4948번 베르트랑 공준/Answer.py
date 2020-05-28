list = [1]*123456*2
list.append(0)
s = int(len(list)*0.5)
for i in range(2,s+1):
    if(list[i]):
        for j in range(i+i,len(list),i):
            list[j] = 0
while(1):
    n = int(input())
    if(not n):break
    count = 0
    for i in range(n+1,2*n+1):
        if(list[i]):
            count+=1
    print(count)





