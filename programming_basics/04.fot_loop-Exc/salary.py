n = int(input())
salary = int(input())

for tabs in range(n):
    name_tab = input()
    if name_tab == "Facebook":
        salary -= 150
    elif name_tab == "Instagram":
        salary -= 100
    elif name_tab == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        break
if salary > 0:
    print(salary)
