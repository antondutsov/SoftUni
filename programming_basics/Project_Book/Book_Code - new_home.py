flowers_type = input()
flowers_pcs = int(input())
budget = int(input())

price = 0

if flowers_type == "Roses":
    price = 5.00
elif flowers_type == "Dahlias":
    price = 3.80
elif flowers_type == "Tulips":
    price = 2.80
elif flowers_type == "Narcissus":
    price = 3.00
elif flowers_type == "Gladiolus":
    price = 2.50
else:
    print("Enter name of flower!")

cost = flowers_pcs * price

discount = 0
if flowers_type == "Roses" and flowers_pcs > 80:
    discount = cost * 0.10
elif flowers_type == "Dahlias" and flowers_pcs > 90:
    discount = cost * 0.15
elif flowers_type == "Tulips" and flowers_pcs > 80:
    discount = cost * 0.15
elif flowers_type == "Narcissus" and flowers_pcs < 120:
    price_increase = cost * 1.15
elif flowers_type == "Gladiolus" and flowers_pcs < 80:
    price_increase = cost * 1.20

total = cost - discount

money_left = budget - total

if budget >= cost:
    print(f"Hey, you have a great garden with {flowers_pcs} {flowers_type} and {total:.2f} leva left")
elif budget < cost:
    money_left = abs(money_left)
    print(f"Not enough money, you need {money_left:.2f} leva more.")
