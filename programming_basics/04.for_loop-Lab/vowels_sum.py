sentence = input()
a = 0
e = 0
i = 0
o = 0
u = 0
total = 0

for char in sentence:
    if char == "a":
        a += 1
    elif char == "e":
        e += 2
    elif char == "i":
        i += 3
    elif char == "o":
        o += 4
    elif char == "u":
        u += 5

total = a + e + i + o + u
print(total)
