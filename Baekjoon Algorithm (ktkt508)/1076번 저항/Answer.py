om = []
om.append({
    "black":0,
    "brown":1,
    "red":2,
    "orange":3,
    "yellow":4,
    "green":5,
    "blue":6,
    "violet":7,
    "grey":8,
    "white":9
})
a = input()
b = input()
c = input()
for color in om:
    a = color[a]
    b = color[b]
    c = color[c]

a = a*10+b
c = 10**c
print(a*c)

