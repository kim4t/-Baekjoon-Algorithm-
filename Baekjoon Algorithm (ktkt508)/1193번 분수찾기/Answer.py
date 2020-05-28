n = int(input())
count = 0
for i in range(1,10000000):
    if(n-i>=0):
        n = n-i
    else:
        count = i-1
        break
remain = n
if (remain!=0):

    if(count%2==0):
        a = count+1
        b = 1
        a = a-remain+1
        b = b+remain-1
    else:
        a = 1
        b = count+1
        a = a+remain-1
        b = b-remain+1

    print(a,end='')
    print('/',end='')
    print(b)
else:
    if(count%2==0):
        print(count, end='')
        print('/', end='')
        print(1)
    else:
        print(1, end='')
        print('/', end='')
        print(count)

