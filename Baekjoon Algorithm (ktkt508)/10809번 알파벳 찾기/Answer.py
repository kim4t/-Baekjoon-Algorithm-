n = input()
a = []
for i in range(26):
    a.append(chr(97+i))
for i in a:
    if(i in n):
        print(n.index(i),end=' ')
    else: print(-1,end=' ')
