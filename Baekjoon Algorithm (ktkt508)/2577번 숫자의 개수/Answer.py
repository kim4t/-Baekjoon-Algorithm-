a = int(input())
b = int(input())
c = int(input())
t = a*b*c
t = str(t)

l = []
for i in range(10):
    l.append(0)

for i in range(len(t)):
    if(t[i]=='0'): l[0]+=1
    elif(t[i]=='1'): l[1]+=1
    elif (t[i] == '2'): l[2] += 1
    elif (t[i] == '3'): l[3] += 1
    elif (t[i] == '4'): l[4] += 1
    elif (t[i] == '5'): l[5] += 1
    elif (t[i] == '6'): l[6] += 1
    elif (t[i] == '7'): l[7] += 1
    elif (t[i] == '8'): l[8] += 1
    else: l[9] += 1
for i in range(10):
    print(l[i])
