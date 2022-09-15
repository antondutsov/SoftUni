n = int(input())

left_sum = 0
right_sum = 0

for number in range(0, n*2):
    input_sum = int(input())
    if number < n:
        left_sum += input_sum
    else:
        right_sum += input_sum

if left_sum == right_sum:
    print('Yes, sum =', left_sum)
else:
    print('No, diff =', abs(left_sum - right_sum))
