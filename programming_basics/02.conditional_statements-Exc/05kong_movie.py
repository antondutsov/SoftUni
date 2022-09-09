# decore = 10% of budget
# >150 crew => 10% off costumes


budget = float(input())
crew = int(input())
p_costume = float(input())
decore = budget * 0.10

p_wear = crew * p_costume

if crew > 150:
    p_wear = (crew * p_costume) * 0.90
production_cost = (p_wear + decore)
total = abs(budget - production_cost)

if budget >= production_cost:
    print("Action!")
    print(f"Wingard starts filming with {total:.2f} leva left.")
elif production_cost > budget:
    print("Not enough money!")
    print(f"Wingard needs {total:.2f} leva more.")
