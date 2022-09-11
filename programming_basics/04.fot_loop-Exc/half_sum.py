import sys

max_num = -999999999999999
sum_numbers = 0
n = int(input())
  
for i in range(0, n):
	num = int(input())

if num > max_size:
	max_num = num
	sum_numbers += num
if man_num == sum_numbers - max_num:
	print('Yes')
	print(f'Sum= {sum_numbers}')
else:
	print('No')
	sum_others = sum_numbers - max_num
	print(f'Diff= {abs(max_num - sum_numbers)}')