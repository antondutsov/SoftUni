bitcoins = int(input()) * 1168
rmb = float(input()) * 0.15
commission = float(input())
euro = 1.95
rmb *= 1.76

amount = (bitcoins + rmb) / euro
# print(amount)
commission = (commission / 100) * amount
# print(commission)

print('%.2f' % (amount - commission))
