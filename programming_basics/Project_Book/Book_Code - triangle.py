n = int(input())

for row in range(0, n):
    print("$", end="")
    for col in range(row):
        print(" $", end="")
    print()
