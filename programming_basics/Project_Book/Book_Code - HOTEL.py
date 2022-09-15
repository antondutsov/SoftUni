exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

delay_hour = 0
delay_minutes = 0

late = 0
on_time = 0
early = 0

if exam_hour <= arrival_time:
    arrival_time - exam_hour = delay_hour
elif exam_hour > arrival_time:
    exam_hour - arrival_time = abs(delay_hour)

if exam_minutes <= arrival_minutes:
    arrival_minutes - exam_minutes = delay_minutes
elif exam_minutes > arrival_minutes:
    exam_minutes - arrival_time = abs(delay_minutes)


    