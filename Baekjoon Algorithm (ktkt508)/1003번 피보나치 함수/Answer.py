t = int(input())
l1 = [1,0]
l2 = [0,1]

for i in range(2,41):
    l1.append(l1[i-1]+l1[i-2])
    l2.append(l2[i-1]+l2[i-2])

for i in range(t):
    n = int(input())
    print(l1[n],l2[n])
