a = int(input())
b = int(input())
a = int(a//100)*100
c = 0
while 1:
    if((a+c)%b==0):
        break
    else: c+=1
if(c<10):
    print('0',end='')
    print(c)
else:
    print(c)
