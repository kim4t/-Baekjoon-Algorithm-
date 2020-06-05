t = int(input())
for i in range(t):
   x,y = map(int,input().split())
   distance = y-x
   n = int((distance-1)**0.5)
   if distance <= n*(n+1):
       print(n*2)
   else:
       print(n*2+1)