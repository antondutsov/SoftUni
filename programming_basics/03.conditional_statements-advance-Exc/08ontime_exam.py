exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
late = "Late"
on_time = "On time"
early = "Early"

exam_time = (exam_hour * 60) + exam_minutes
arrival_time = (arrival_hour * 60) + arrival_minutes

total_minutes_difference = arrival_time - exam_time

student_arrival = late
if total_minutes_difference < -30:
    student_arrival = early
elif total_minutes_difference <= 0:
    student_arrival = on_time

result = ""
if total_minutes_difference != 0:
    hours_difference = abs(total_minutes_difference) // 60
    minutes_difference = abs(total_minutes_difference) % 60
    if hours_difference > 0:
        result = f"{hours_difference}:{minutes_difference:02} hours"
    else:
        result = f"{minutes_difference} minutes"
    if total_minutes_difference < 0:
        result += " before the start"
    else:
        result += " after the start"

print(student_arrival)
if result:
    print(result)
