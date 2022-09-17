sentence = input().lower()

words = ['sand', 'water', 'fish', 'sun']
counter = 0

for item in words:
    if item in sentence:
        counter += 1

print(counter)
