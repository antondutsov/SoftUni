work_days = int(input())
daily_earnings = float(input())
exchange_rate = float(input())

montly_earnings = work_days * daily_earnings
yearly_earnings = montly_earnings * 12 + montly_earnings * 2.5
tax_deduction = (25 / 100) * yearly_earnings
total = (yearly_earnings - tax_deduction)* exchange_rate
print('%.2f' % (total / 365))
