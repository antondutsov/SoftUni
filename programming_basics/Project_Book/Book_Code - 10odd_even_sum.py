n = int(input())

left_sum = 0
right_sum = 0

for i in range(0, n):
    input_sum = int(input())
    if i % 2 == 0:
        right_sum += input_sum
    else:
        left_sum += input_sum
        
if left_sum == right_sum:
    print('Yes\nSum =', right_sum)
else:
    print('No\nDiff =', abs(right_sum - left_sum))

#n = int(input())

#left_sum = 0
#right_sum = 0

#for i in range(0, n):
    #input_sum = int(input())
    #if i % 2 == 0:
        #right_sum += input_sum
    #else:
        #left_sum += input_sum
        
#if left_sum == right_sum:
    #print('Sum = ', right_sum)
#else:
    #print('Diff = ', abs(right_sum - left_sum))
