input_number = int(input())

max_num = -1000000000000000

for i in range(0, input_number):
    num = int(input())
    if num > max_num:
        max_num = num
print(max_num)
