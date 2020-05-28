n = int(input())
for i in range(n):
    l = input().split()
    del(l[0])
    total=0
    for j in range(len(l)):
        l[j] = int(l[j])
        total+=l[j]
    avg = total/len(l)
    count = 0
    for j in range(len(l)):
        if(l[j]>avg):
            count+=1
    p = count/len(l)*100
    p = round(p,3)
    print('%.3f' % p,end='')
    print('%')