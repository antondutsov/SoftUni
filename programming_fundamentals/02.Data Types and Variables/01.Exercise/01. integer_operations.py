counter = 0
total = 0

while counter < 4:
    counter += 1
    number = int(input())
    if counter == 1:
        total = number
    elif counter == 2:
        total += number
    elif counter == 3:
        total /= number
        total = int(total)
    elif counter == 4:
        total *= number
print('{:.0f}'.format(total))
