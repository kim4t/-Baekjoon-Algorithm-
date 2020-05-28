s = input()
c = ['c=','c-','dz=','d-','lj','nj','s=','z=']
count = 0
count2 = 0
for i in range(len(c)):
    if(c[i] in s):
        count+= s.count(c[i])
        count2+= len(c[i])*s.count(c[i])


print(len(s)-count2+count+s.count(c[2]))




