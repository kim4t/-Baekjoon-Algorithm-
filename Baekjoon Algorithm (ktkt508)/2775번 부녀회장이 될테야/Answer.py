l = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
for i in range(15):
    l[0].append(i+1)


for i in range(1,15):
    v = 0
    for j in l[i-1]:
        v+=j
        l[i].append(v)

n = int(input())
for i in range(n):
    f = int(input())
    r = int(input())
    print(l[f][r-1])



