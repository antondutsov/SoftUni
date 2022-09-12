max_number = -2**63

while True:
    command = input()
    if command == 'Stop':
        break
    else:
        if int(command) > int(max_number):
            max_number = command
print(max_number)
