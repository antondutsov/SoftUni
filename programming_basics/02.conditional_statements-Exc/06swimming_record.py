import math

record_time = float(input())
distance = float(input())
time_per_meter = float(input())

distance_time = distance * time_per_meter

current = math.floor((distance / 15)) * 12.5

swimming_time = distance_time + current

difference = swimming_time - record_time

if swimming_time < record_time:
    print(f"Yes, he succeeded! The new world record is {swimming_time:.2f} seconds.")
elif swimming_time >= record_time:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")