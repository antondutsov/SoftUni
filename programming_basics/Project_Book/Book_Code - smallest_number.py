input_number = int(input())

min_num = 1000000000000000

for i in range(0, input_number):
    num = int(input())
    if num < min_num:
        min_num = num
print(min_num)