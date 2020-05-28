import sys
a = int(input())
for x in range(a):
    b,c = sys.stdin.readline().rstrip().split()
    print(int(b)+int(c))