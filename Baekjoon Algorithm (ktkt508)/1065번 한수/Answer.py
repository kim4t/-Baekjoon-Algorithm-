n = int(input())
total = 0
for i in range(1,n+1):
    if(i<100):
        total+=1
    else:
        strNum = str(i)
        length = len(strNum)
        gap = int(strNum[1]) - int(strNum[0])
        han = True
        for j in range(length-1):
            if(int(strNum[j+1])-int(strNum[j])!=gap):
                han = False
                break
        if(han):
            total+=1

print(total)




