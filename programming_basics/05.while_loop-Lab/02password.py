#user_name = input()
#password = input()
 
#data = input()
 
#while data != password:
    #data = input()
    #if data == password:
        #break
    #print('Welcome', user_name)
 
# това е аутпутът, който въвеждам и когато въведа 1324, програмата приема, че е вярна парола. Бих искал да зная защо работи грешно?
#Dutsov - user_name
#1234 - password
#pass - въведена стойност
#1324 - въведена стойност, която се приема, че е вярна
#Welcome  Dutsov - програмата приключва след въведена грешна стойност


username = input()
password = input()

data = input()
while data != password:
    data = input()
print(f"Welcome {username}!")
