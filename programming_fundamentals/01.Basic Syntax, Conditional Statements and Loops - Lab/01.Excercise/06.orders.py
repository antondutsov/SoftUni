# You work at a coffee shop, and your job is to place orders to the
# distributors. Thus, you want to know the price of each order. On the first
# line, you will receive integer N – the number of orders the shop will
# receive.
# For each order, you will receive the following information:You work at a
# coffee shop, and your job is to place orders to the distributors. Thus,
# you  want to know the price of each order. On the first line, you will
# receive integer N – the number of orders the shop will receive. For
# each order, you will receive the following information:

orders = int(input())

total_price = 0

for order in range(orders):
    capsule_price = float(input())
    days = int(input())
    capsule_count = int(input())
    price = (capsule_price * capsule_count) * days
    print(f'The price for the coffee is: ${price:.2f}')
    total_price += price
print(f'Total: ${total_price:.2f}')


