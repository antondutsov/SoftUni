# Kids drink toddy, teens drink coke, young adults drink beer, and adults
# drink  whisky. Create a program that receives an age and prints what
# they drink.

age = int(input())

if age < 15:
    print('drink toddy')
elif age < 19:
    print('drink coke')
elif age < 22:
    print('drink beer')
else:
    print('drink whisky')
