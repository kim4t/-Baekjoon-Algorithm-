n,m = map(int,input().split())
list = list(map(int,input().split()))
max = 0
for i in range(len(list)):
    for j in range(i+1,len(list)):
        for k in range(j+1,len(list)):
            sum = list[i]+list[j]+list[k]
            if(sum>max and sum<=m):
                max = sum
print(max)