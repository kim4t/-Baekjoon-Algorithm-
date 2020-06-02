n = int(input())
max = 10000000
two = [2,4,8,6]
three = [3,9,7,1]
four = [4,6]
seven = [7,9,3,1]
eight = [8,4,2,6]
nine = [9,1]

for i in range(n):
    a,b = input().split()
    a = int(a[len(a)-1])
    b= int(b)
    if(a==1 or a==5 or a==6):
        print(a)
    elif (a == 2):
        r = b%4
        print(two[r-1])
    elif (a == 3):
        r = b%4
        print(three[r-1])
    elif (a == 4):
        r= b%2
        print(four[r-1])
    elif (a == 7):
        r = b % 4
        print(seven[r-1])
    elif (a == 8):
        r = b % 4
        print(eight[r-1])
    elif (a == 9):
        r = b % 2
        print(nine[r-1])
    else: print(10)




