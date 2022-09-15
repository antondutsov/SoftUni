import math

l = float(input()) * 100
w = float(input()) * 100

rows = math.trunc(l / 120)
columns = math.trunc((w - 100) / 70)

seating_places = rows * columns - 3

print(seating_places)