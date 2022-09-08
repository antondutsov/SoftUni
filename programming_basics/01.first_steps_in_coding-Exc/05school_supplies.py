pencils_pack = int(input()) * 5.80
markers_pack = int(input()) * 7.20
detergent = int(input()) * 1.20
discount = int(input()) / 100

price = pencils_pack + markers_pack + detergent
total = price - (price * discount)

print(total)


