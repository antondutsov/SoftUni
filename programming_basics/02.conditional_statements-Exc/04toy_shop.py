# puzzle = 2.60
# doll = 3.00
# teddy = 4.10
# minion = 8.20
# truck = 2.00

# order >= 50pcs => 25% off
# from order 10% rent => rent = 10% from 'total'

p_trip = float(input())
qpuzzles = int(input())
qdolls = int(input())
qteddies = int(input())
qminions = int(input())
qtrucks = int(input())

p_puzzle = qpuzzles * 2.60
p_dolls = qdolls * 3.00
p_teddies = qteddies * 4.10
p_minions = qminions * 8.20
p_trucks = qtrucks * 2.00

q_total = qpuzzles + qdolls + qteddies + qminions + qtrucks
p_total = p_trucks + p_minions + p_puzzle + p_teddies + p_dolls

if q_total >= 50:
    p_total = p_total * 0.75

rent = p_total - (p_total * 0.90)

profit = p_total - rent

money_left = profit - p_trip

if profit >= p_trip:
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_left = abs(money_left)
    print(f"Not enough money! {money_left:.2f} lv needed.")
