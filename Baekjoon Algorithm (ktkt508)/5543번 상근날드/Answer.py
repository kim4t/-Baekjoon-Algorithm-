minham = 2000
for i in range(3):
    l = int(input())
    if(l<minham):
        minham = l
minbev = 2000
for i in range(2):
    l = int(input())
    if(l<minbev):
        minbev = l
print(minham+minbev-50)