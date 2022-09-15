numbers = int(input())

p1 = 0  # divide by 2
p2 = 0  # divide by 3
p3 = 0  # divide by 4

divisible_by_2 = 0
divisible_by_3 = 0
divisible_by_4 = 0

for num in range(0, numbers):
    number_sequence = int(input())
    if number_sequence % 2 == 0:
        p1 += 1
    if number_sequence % 3 == 0:
        p2 += 1
    if number_sequence % 4 == 0:
        p3 += 1

print("{0:.2f}%".format(p1 / numbers * 100))
print("{0:.2f}%".format(p2 / numbers * 100))
print("{0:.2f}%".format(p3 / numbers * 100))
