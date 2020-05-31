t = int(input())
s = input().split()
for i in range(t):
    s[i] = int(s[i])
s.sort()
print(s[0]*s[len(s)-1])

