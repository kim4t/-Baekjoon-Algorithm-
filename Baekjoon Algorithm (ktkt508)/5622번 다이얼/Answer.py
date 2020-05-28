s = input().lower()
l = [['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],
     ['t','u','v'],['w','x','y','z']]
word = 0
for i in range(len(s)):
    if(s[i] in l[0]):
        word+=3
    elif(s[i] in l[1]):
        word+= 4
    elif (s[i] in l[2]):
        word += 5
    elif (s[i] in l[3]):
        word += 6
    elif (s[i] in l[4]):
        word += 7
    elif (s[i] in l[5]):
        word += 8
    elif (s[i] in l[6]):
        word += 9
    elif (s[i] in l[7]):
        word += 10
print(word)
