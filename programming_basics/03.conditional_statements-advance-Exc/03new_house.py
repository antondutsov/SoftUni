flowers = input()
count = int(input())
budget = int(input())

price = 0

if flowers == "Roses":
    price = count * 5.00
    if count > 80:
        price *= 0.9
elif flowers == "Dahlias":
    price = count * 3.80
    if count > 90:
        price *= 0.85
elif flowers == "Tulips":
    price = count * 2.80
    if count > 80:
        price *= 0.85
elif flowers == "Narcissus":
    price = count * 3.00
    if count < 120:
        price *= 1.15
elif flowers == "Gladiolus":
    price = count * 2.50
    if count < 80:
        price *= 1.20
else:
    print("Enter flower name!")

difference = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {count} {flowers} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
