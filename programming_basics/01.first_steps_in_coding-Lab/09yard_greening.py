garden = float(input())
price = 7.61
discount = 0.18

cost = garden * price
discount = cost * discount
total = cost - discount
# print(f"{cost} \n{discount}\n{total}")
print(f"The final price is: {total} lv.\nThe discount is: {discount} lv.")
