first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time = first_time + second_time + third_time

minutes = total_time // 60
seconds = total_time % 60

if minutes < 10:
    print("{0:0}:{1:02}".format(minutes, seconds))
else:
    print("{0:1}:{1:02}".format(minutes, seconds))
