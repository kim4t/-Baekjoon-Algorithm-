a,b,c = map(int, input().split())
if(c<=b): print(-1)
else:
    p = a//(c-b)
    print(p+1)


