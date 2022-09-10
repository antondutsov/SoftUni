budget = float(input())
season = input()

destination = ""
place = ""

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget *= 0.3
        place = "Camp"
    else:
        budget *= 0.7
        place = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget *= 0.4
        place = "Camp"
    else:
        budget *= 0.8
        place = "Hotel"
elif budget > 1000:
    budget *= 0.9
    destination = "Europe"
    place = "Hotel"
else:
    print("Enter budget!")

print(f"Somewhere in {destination}\n{place} - {budget:.2f}")



