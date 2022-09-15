p_vegetables = float(input())
p_fruits = float(input())
w_vegetables = int(input())
w_fruits = int(input())

euro_p = 1.94

vegetables_cost = p_vegetables * w_vegetables
fruits_cost = p_fruits * w_fruits

total_cost = vegetables_cost + fruits_cost

total_price = total_cost / euro_p

print(total_price)
