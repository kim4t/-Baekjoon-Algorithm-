n = int(input())
top = 2*n-1
for i in range(top//2):
    print(' '*i,end='')
    print('*'*(top-(2*i)))
for i in range(1,top//2+2):
    print(' '*((top//2)-i+1),end='')
    print('*'*((2*i)-1))