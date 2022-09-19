range_from = int(input())
range_till = int(input())

for i in range(range_from, range_till+1):
    print(f'{chr(i)}', end=' ')
