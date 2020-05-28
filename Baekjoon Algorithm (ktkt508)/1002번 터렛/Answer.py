import math
n = int(input())
i = 0;
while i<n:
    x1,y1,r1,x2,y2,r2 = map(int, input().split())
    d = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1,2))
    if x1==x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)

    else:

            if r2 > r1:
                t = r1
                r1 = r2
                r2 = t
            if d == r1 + r2:
                print(1)

            elif r1 - r2 < d < r1 + r2:
                print(2)

            elif d > r1 + r2:
                print(0)

            elif d == r1 - r2:
                print(1)

            elif d < r1 - r2:
                print(0)

    i+=1