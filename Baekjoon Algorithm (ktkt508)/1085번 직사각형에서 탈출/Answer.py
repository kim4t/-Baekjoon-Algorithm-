x,y,w,h = map(int,input().split())
list = []
list.append(w-x)
list.append(h-y)
list.append(x)
list.append(y)
print(min(list))