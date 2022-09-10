budget = int(input())
season = input()
fisherman = int(input())

boat_rent = 0

if season == "Spring":
    boat_rent = 3000
elif "Winter" == season:
    boat_rent = 2600
elif season == "Summer" or "Autumn":
    boat_rent = 4200
else:
    print("Enter season!")

if 6 >= fisherman:
    boat_rent *= 0.90
elif 7 <= fisherman <= 11:
    boat_rent *= 0.85
else:
    boat_rent *= 0.75

if season != "Autumn":
    if fisherman % 2 == 0:
        boat_rent *= 0.95

difference = abs(budget - boat_rent)

if budget >= boat_rent:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
