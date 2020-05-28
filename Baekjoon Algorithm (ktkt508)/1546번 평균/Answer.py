n = int(input())
max=0
l = []
l = input().split()
for i in range(n):
    l[i] = int(l[i])
    if(l[i]>max):
        max = l[i]
total = 0

for i in range(len(l)):
    l[i] = l[i]*100
    l[i] = l[i]/max
    total+=l[i]

print(total/n)