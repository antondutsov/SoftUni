heritage = float(input())
year_to_live = int(input())
years = 18

for current_year in range(1800, year_to_live+1):
    if current_year % 2 == 0:
        heritage -= 12000
    else:
        heritage -= (12000 + 50 * years)
    years += 1

diff = abs(heritage)

if heritage >= 0:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')
else:
    print(f'He will need {diff:.2f} dollars to survive.')
