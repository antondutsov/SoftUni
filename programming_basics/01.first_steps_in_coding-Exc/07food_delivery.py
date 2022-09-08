chicken_menu = int(input()) * 10.35
fish_menu = int(input()) * 12.40
vegi_menu = int(input()) * 8.15
order_total = chicken_menu + fish_menu + vegi_menu
desert = order_total * 0.20

total = order_total + desert + 2.50
print(total)
