dog_food = int(input())
cat_food = int(input())
dog_food_price = 2.50
cat_food_price = 4

total = (dog_food * dog_food_price) + (cat_food * cat_food_price)

#print(f"{total} lv.")
print("%.1f lv." % total)
