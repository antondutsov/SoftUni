year_fee = int(input())

snickers = year_fee - (year_fee * 0.40)
equipment = snickers - (snickers * 0.20)
basket_ball = equipment - (equipment * 0.75)
accessories = basket_ball - (basket_ball * 0.80)

total = year_fee + snickers + equipment + basket_ball + accessories
print(total)
