key = int(input())
lines = int(input())

decoded = ''

for line in range(lines):
    word = input()
    word = ord(word) + key
    word = chr(word)
    decoded += '' + word
print(decoded)
