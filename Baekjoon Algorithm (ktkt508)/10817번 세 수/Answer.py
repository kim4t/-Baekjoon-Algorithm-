a,b,c = map(int, input().split())
l = []
l.append(a)
l.append(b)
l.append(c)
max = 0
min = 100
for i in l:
    if(i>max):
        max = i
    if(i<min):
        min = i
l.remove(max)
l.remove(min)
print(l[0])