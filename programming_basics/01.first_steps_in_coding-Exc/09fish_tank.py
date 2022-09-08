width = int(input())
length = int(input())
height = int(input())
percent = float(input()) / 100

volume = width * length * height
volume_liters = volume / 1000

water_capacity = volume_liters * (1 - percent)

print(water_capacity)
