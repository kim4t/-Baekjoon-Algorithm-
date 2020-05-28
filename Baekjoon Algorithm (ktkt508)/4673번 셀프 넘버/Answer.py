list = []
d = []
for i in range(1,10000):
    list.append(i)
for i in range(9999):
    num = list[i]
    strNum = str(num)
    length = len(strNum)
    total = 0
    for j in range(length):
        total+=int(strNum[j])
    total+=num
    d.append(total)
for i in list:
    if(i not in d):
        print(i)