flowers = input()
count = int(input())
#budget = int(input())

price = 0
discount = 0

if flowers == "Roses":
    price = 5.00
    if count > 80:
        discount = (count * price) * 0.10
elif flowers == "Dahlias":
    price = 3.80
    if count > 90:
        discount = (count * price) * 0.15
elif flowers == "Tulips":
    price = 2.80
    if count > 80:
        discount = (count * price) * 0.15
elif flowers == "Narcissus":
    price = 3.00
    if count < 120:
        discount = count * (price * 0.15)
elif flowers == "Gladiolus":
    price = 2.50
    if count < 80:
        discount = (count * price) * 1.20
else:
    print("Enter flower name!")
    

        