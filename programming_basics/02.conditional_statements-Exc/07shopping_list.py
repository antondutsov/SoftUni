budget = float(input())
vc = int(input())
cpu = int(input())
ram = int(input())

p_vc = 250
p_cpu = (p_vc * vc) * 0.35  # 87.50
p_ram = (p_vc * vc) * 0.10  # 25.00

p_total = (vc * p_vc) + (cpu * p_cpu) + (ram * p_ram)

if vc > cpu:
    p_total = p_total - (p_total * 0.15)

total = budget - p_total

if budget >= p_total:
    print(f"You have {total:.2f} leva left!")
else:
    total = abs(total)
    print(f"Not enough money! You need {total:.2f} leva more!")
