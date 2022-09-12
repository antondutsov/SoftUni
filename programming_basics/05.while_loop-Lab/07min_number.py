min_number = 2**63

while True:
    command = input()
    if command == 'Stop':
        break
    else:
        if int(command) < int(min_number):
            min_number = command
print(min_number)
