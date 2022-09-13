num1 = int(input())
num2 = int(input())
magic_num = int(input())
counter = 0
combination_found = False

for first_number in range(num1, num2 + 1):
    for second_number in range(num1, num2 + 1):
        counter += 1
        if first_number + second_number == magic_num:
            combination_found = True
            break
    if combination_found:
        break
if combination_found:
    print(f'Combination N:{counter} ({first_number} + {second_number} = {magic_num})')
else:
    print(f'{counter} combinations - neither equals {magic_num}')
