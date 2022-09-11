n = int(input())

for num in range(0, n+1):
    i = pow(2, num)
    if num % 2 == 0:
        print(i)
