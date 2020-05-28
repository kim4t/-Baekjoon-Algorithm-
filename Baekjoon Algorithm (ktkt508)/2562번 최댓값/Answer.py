l = []
for i in range(9):
    l.append(int(input()))
max = 0
index = 0
for i in range(9):
    if(l[i]>max):
        max = l[i]
        index = i
print(max)
print(index+1)
