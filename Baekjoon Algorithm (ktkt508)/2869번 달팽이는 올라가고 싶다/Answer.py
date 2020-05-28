a,b,v = map(int,input().split())
h = v-a
u = a-b
if(h% u==0):
    h = h//u
else:
    h = (h//u)+1
print(h+1)