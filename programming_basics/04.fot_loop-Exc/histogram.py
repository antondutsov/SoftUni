numbers = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for number in range(0, numbers):
    current_number = int(input())
    if 200 > current_number:
        p1 += 1
    elif 200 <= current_number <= 399:
        p2 += 1
    elif 400 <= current_number <=599:
        p3 += 1
    elif 600 <= current_number <= 799:
        p4 += 1
    else:
        p5 += 1
print("{0:.2f}%".format(p1 / numbers * 100))
print("{0:.2f}".format(p2 / numbers * 100))
print("{0:.2f}".format(p3 / numbers * 100))
print("{0:.2f}".format(p4 / numbers * 100))
print("{0:.2f}".format(p5 / numbers * 100))

