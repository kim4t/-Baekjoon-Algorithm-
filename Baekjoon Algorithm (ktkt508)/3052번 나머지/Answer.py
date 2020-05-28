set = set([])
for i in range(10):
    num = int(input())
    num = num%42
    set.add(num)
print(len(set))