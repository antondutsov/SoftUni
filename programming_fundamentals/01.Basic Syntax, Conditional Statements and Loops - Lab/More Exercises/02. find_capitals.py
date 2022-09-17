sentence = input()
indices = []
capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N',  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y',  'Z']
count = -1

for letter in sentence:
    count += 1
    if letter in capitals:
        indices.append(count)
print(indices)
