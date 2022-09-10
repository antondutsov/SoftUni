month = input()
overnight = int(input())

studio_rent = 0
apartment_rent = 0

if month == "May" or month == "October":
    studio_price = 50.00
    apartment_price = 65.00
    studio_rent = studio_price * overnight
    apartment_rent = apartment_price * overnight
    if overnight > 14:
        studio_rent *= 0.70
        apartment_rent *= 0.90
    elif overnight > 7:
        studio_rent *= 0.95
elif month == "June" or month == "September":
    studio_price = 75.20
    apartment_price = 68.70
    studio_rent = studio_price * overnight
    apartment_rent = apartment_price * overnight
    if overnight > 14:
        studio_rent *= 0.80
        apartment_rent *= 0.90
else:
    if month == "July" or month == "August":
        studio_price = 76
        apartment_price = 77
        studio_rent = studio_price * overnight
        apartment_rent = apartment_price * overnight
    if overnight > 14:
        apartment_rent *= 0.90

apartment_info = f"Apartment: {apartment_rent:.2f} lv."
studio_info = f"Studio: {studio_rent:.2f} lv."

print(apartment_info)
print(studio_info)
#
# if month == "May" or month == "October":
#     studio = 50 * overnight
#     apartment = 65 * overnight
#     if overnight > 14:
#         apartment *= 0.90
#         studio *= 0.70
#     elif overnight > 7:
#         apartment *= 0.9
# elif month == "June" or month == "September":
#     studio = 75.20 * overnight
#     apartment = 68.70 * overnight
#     if overnight > 14:
#         studio *= 0.80
#         apartment *= 0.9
# elif month == "July" or month == "August":
#     studio = 76 * overnight
#     apartment = 77 * overnight
#     if overnight > 14:
#         apartment *= 0.9
#
# print(f"Apartment: {apartment:.2f} lv.")
# print(f"Studio: {studio:.2f} lv.")
