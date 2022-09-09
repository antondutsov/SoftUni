import math
series = str(input())
series_time = int(input())
break_time = int(input())

time_for_lunch = break_time * 1/8
time_for_rnr = break_time * 1/4
time_remaining = break_time - time_for_lunch - time_for_rnr

time_needed = time_remaining - series_time

if time_remaining >= series_time:
    print(f"You have enough time to watch {series} and left with {math.ceil(time_needed)} minutes free time.")
else:
    time_needed = abs(time_needed)
    print(f"You don't have enough time to watch {series}, you need {math.ceil(time_needed)} more minutes.")
