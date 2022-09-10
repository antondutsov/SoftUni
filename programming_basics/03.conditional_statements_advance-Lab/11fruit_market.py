#fruit = input()
week_day = input()
#amount = float(input())

if (week_day == 'Monday' or week_day == 'Tuesday' or week_day == 'Wednesday' or  week_day == 'Thursday' or week_day == 'Friday'):
    week_day_prices = {2.50: 'banana', 1.20: 'apple', 0.85: 'orange', 1.45: 'grapefruit', 2.70: 'kiwi', 5.50: 'pineapple', 3.85: 'grapes'}
elif week_day == 'Saturday' or week_day == 'Sunday':
    weekend_prices = {2.70: 'banana', 1.25: 'apple', 0.90: 'orange', 1.60: 'grapefruit', 3.00: 'kiwi', 5.60: 'pineapple', 4.20: 'grapes'}
