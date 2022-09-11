age = int(input())  # 7
washing_machine = float(input())  #600.00
toy_price = int(input())  # 10

toy_count = 0
sum = 0

money = 0
brother_money = 0

for year in range(1, age+1):  # from 0 to 7
    if year % 2 == 0:
        money = money + 10
        sum += money
        brother_money += 1
    else:
        toy_count += 1

sum = sum + toy_count * toy_price - brother_money

if sum >= washing_machine:
    diff = sum - washing_machine
    print(f"Yes! {diff:.2f}")
else:
    diff = washing_machine - sum
    print(f"No! {diff:.2f}")
