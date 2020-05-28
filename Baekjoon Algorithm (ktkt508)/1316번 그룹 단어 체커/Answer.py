n = int(input())
total = 0
for i in range(n):
    s = input()
    l = []
    c = True
    if(len(s)<3):
        total+=1
    else:
        l.append(s[0])
        l.append(s[1])
        for j in range(2,len(s)):
            if(s[j] not in l):
                l.append(s[j])
            else:
                if(s[j]!=s[j-1] and s[j] in l):
                    c = False
                    break
        if(c): total+=1
print(total)



