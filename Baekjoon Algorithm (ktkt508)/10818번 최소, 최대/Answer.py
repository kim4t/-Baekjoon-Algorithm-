n = int(input())
l = input().split()
arr = []
for i in range(n):
    arr.append(int(l[i]))
arr.sort()
print(arr[0],arr[n-1])