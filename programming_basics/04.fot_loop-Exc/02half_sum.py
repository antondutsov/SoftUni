n = int(input())

max_num = -2**63-1
sum_numbers = 0


for i in range(0, n):
    input_number = int(input())
    sum_numbers += input_number
    if input_number > max_num:
        max_num = input_number
        
if max_num == sum_numbers - max_num:
    print('Yes\nSum =', max_num)
else:
    diff = abs(max_num - (sum_numbers - max_num))
    print('No\nDiff =', diff)
