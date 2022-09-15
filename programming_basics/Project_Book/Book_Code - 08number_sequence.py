n = int(input())

max_num = -9223372036854775807
min_num =  9223372036854775807

for i in range(0, n):
    input_number = int(input())
    if input_number > max_num:
        max_num = input_number
    if input_number < min_num:
        min_num = input_number
        
print(f'Max number: {max_num}')
print(f'Min number: {min_num}')
