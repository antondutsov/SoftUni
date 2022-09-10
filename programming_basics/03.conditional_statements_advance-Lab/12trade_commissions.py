# Град		0 ≤ s ≤ 500	500 < s ≤ 1 000	1 000 < s ≤ 10 000	s > 10 000
# Sofia			5%				7%				8%				12%
# Varna			4.5%			7.5%			10%				13%
# Plovdiv		5.5%			8%				12%				14.5%

city = input()
revenue = float(input())

commission = 0
if city == "Sofia":
    if 0 <= revenue <= 500:
        commission = revenue * 0.05
    elif 500 < revenue <= 1000:
        commission = revenue * 0.07
    elif 1000 < revenue <= 10000:
        commission = revenue * 0.08
    elif revenue > 10000:
        commission = revenue * 0.12
elif city == "Varna":
    if 0 <= revenue <= 500:
        commission = revenue * 0.045
    elif 500 < revenue <= 1000:
        commission = revenue * 0.075
    elif 1000 < revenue <= 10000:
        commission = revenue * 0.10
    elif revenue > 10000:
        commission = revenue * 0.13
elif city == "Plovdiv":
    if 0 <= revenue <= 500:
        commission = revenue * 0.055
    elif 500 < revenue <= 1000:
        commission = revenue * 0.08
    elif 1000 < revenue <= 10000:
        commission = revenue * 0.12
    elif revenue > 10000:
        commission = revenue * 0.145

if commission <= 0:
    print('error')
else:
    print(f'{commission:.2f}')
