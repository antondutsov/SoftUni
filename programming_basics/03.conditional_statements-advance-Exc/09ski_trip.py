days = int(input()) - 1
accommodation = input()
rating = input()

one_person_rent = 0
apartment_rent = 0
president_suit_rent = 0

if accommodation == "room for one person":
    one_person_rent = days * 18.00
    price = one_person_rent
elif accommodation == "apartment":
    apartment_rent = days * 25.00
    if days > 15:
        apartment_rent *= 0.50
    elif 10 <= days <= 15:
        apartment_rent *= 0.65
    else:
        if 10 > days:
            apartment_rent *= 0.70
    price = apartment_rent
else:
    if accommodation == "president apartment":
        president_suit_rent = days * 35
        if 15 < days:
            president_suit_rent *= 0.80
        elif 10 < days <= 15:
            president_suit_rent *= 0.75
        else:
            if 10 > days:
                president_suit_rent *= 0.9
    price = president_suit_rent

if rating == "positive":
    total = price * 1.25
else:
    total = price * 0.90

print(f"{total:.2f}")
