repeats = int(input())

for i in range(repeats):
    for j in range(repeats):
        for k in range(repeats):
            print(f'{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}')
