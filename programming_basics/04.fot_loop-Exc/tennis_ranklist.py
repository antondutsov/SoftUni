from math import floor

tournaments = int(input())
starting_points = int(input())

Winnings = 0
w = 0
f = 0
sf = 0

for matches in range(tournaments):
    finnished = input()
    if finnished == "W":
        starting_points += 2000
        w += 2000
        Winnings += 1
    elif finnished == "F":
        starting_points += 1200
        f += 1200
    elif finnished == "SF":
        starting_points += 720
        sf += 720

print(f"Final points: {starting_points}")
print("Average points: {0:.0f}".format(floor((w + f + sf) / tournaments)))
print("{0:.2f}%".format(Winnings / tournaments * 100))
