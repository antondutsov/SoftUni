deposit = float(input())
term = int(input())
interest_rate = float(input()) / 100

month_interest_rate = deposit * interest_rate
total = deposit + (term * ((deposit * interest_rate) / 12))

print(total)
