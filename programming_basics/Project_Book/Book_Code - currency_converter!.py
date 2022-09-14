amount = float(input())
f_cur = input()
t_cur = input()

bgn = 1
usd = 1.79549
eur = 1.95583
gbp = 2.53405

if f_cur == 'BGN' and t_cur == 'BGN':
    print(amount * bgn)
elif f_cur == 'BGN' and t_cur == 'USD':
    print(amount * usd)
elif f