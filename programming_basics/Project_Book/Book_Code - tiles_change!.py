square_side = int(input())
tile_w = float(input())
tile_l = float(input())
bench_w = int(input())
bench_l = int(input())

bench_area = bench_w * bench_l
patio_area = square_side ** 2 - bench_area
tiles_area = tile_w * tile_l
tiles_count = patio_area / tiles_area
# print('%.2f' %tiles_count)

time_spend = 0.20 * tiles_count
# print('%.2f' %time_spend)

print(round(tiles_count, 2))
print(round(time_spend, 2))
