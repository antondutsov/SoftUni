first_name = input()
last_name = input()
age = int(input())
town = input()

#print(f"You are {first_name} {last_name}, a {age}-years old person from {town}.")
print("You are %s %s, a %d-years old person from %s." %(first_name, last_name, age, town))
