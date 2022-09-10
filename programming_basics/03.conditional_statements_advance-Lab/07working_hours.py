time = int(input())
day = input()

open = "open"
closed = "closed"

if day == "Monday":
    if 10 <= time <= 18:
        result = open
    else:
        result = closed
elif day == "Tuesday":
    if 10 <= time <= 18:
        result = open
    else:
        result = closed
elif day == "Wednesday":
    if 10 <= time <= 18:
        result = open
    else:
        result = closed
elif day == "Thursday":
    if 10 <= time <= 18:
        result = open
    else:
        result = closed
elif day == "Friday":
    if 10 <= time <= 18:
        result = open
    else:
        result = closed
elif day == "Saturday":
    if 10 <= time <= 18:
        result = open
    else:
        result = closed
else:
    result = closed

print(result)
