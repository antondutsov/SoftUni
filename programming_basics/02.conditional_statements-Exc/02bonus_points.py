# до 100 = 5 точки
# над 100 += 20%
# над 1000 += 10%
# за четно число + 1 точка
# за завършващо на "5" + 2 точки
# -> 20 => 6; 26
# -> 175 => 37.0; 212.0


# number % 10 == 5

number: int = int(input())
bonus = 0
if number <= 100:
    bonus = 5
    if 0 == number % 2:
        bonus += 1
    elif 5 == number % 10:
        bonus += 2
elif number > 1000:
    bonus = 0.1 * number
else:
    bonus = 0.2 * number

# if number % 2 == 0:
#     bonus += 1
# elif number % 10 == 5:
#     bonus += 2

print(bonus)
print(number + bonus)
