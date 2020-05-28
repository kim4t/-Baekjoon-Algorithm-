n = input().upper()
char = []
number = []
for i in range(len(n)):
    c = n[i]
    if(c not in char):
        char.append(c)
        count = 1
        for j in range(i+1,len(n)):
            if(n[j]==c):
                count+=1
        number.append(count)
max = 0
maxIndex =0
for i in range(len(number)):
    if(number[i]>max):
        max = number[i]
        maxIndex = i
number.remove(max)
if(max in number): print('?')
else:
    print(char[maxIndex])

