n = int(input())
for i in range(n):
    d,l = input().split()
    for j in range(len(l)):
        for k in range(int(d)):
            print(l[j],end='')
    print()
