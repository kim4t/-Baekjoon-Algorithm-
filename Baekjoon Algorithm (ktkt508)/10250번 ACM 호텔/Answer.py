n = int(input())
for i in range(n):
    h,w,n = map(int,input().split())
    count = n//h+1
    floor = n%h
    if(floor ==0):
        count-=1
        floor =h
    p = str(floor)
    if(count<10):
        p+='0'
    p+=str(count)
    print(p)