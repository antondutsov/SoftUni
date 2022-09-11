num_input = int(input()) # 3

left_sum = 0
right_sum = 0

for i in range(0, num_input): # from 0 to 3
    left_input = int(input())
    left_sum += left_input
    
for i in range(0, num_input):
    right_input = int(input())
    right_sum += right_input
   
total = abs(left_sum - right_sum)

if total == 0:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {total}")
    
#print(left_sum)
#print(right_sum)