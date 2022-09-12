balance = 0

while True:
    amount = input()
    if amount == 'NoMoreMoney':
        break
    elif float(amount) < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {float(amount):.2f}')
    balance += float(amount)
    
print(f'Total: {balance:.2f}')