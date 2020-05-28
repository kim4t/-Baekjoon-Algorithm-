a,b = map(int,input().split())
if b>=45:
    print(a,b-45)
else:
    c = 45-b
    if a==0:
        print(23,60-c)
    else:  print(a-1, 60-c)