wight = int(input())
length = int(input())
height = int(input())

volume = wight * length * height
command = ''

while command != 'Done' and volume > 0:
    command = input()
    if command.isnumeric():
        command = int(command)
    if command == 'Done':
        break
    else:
        volume -= command

if volume > 0:
    print(f'{volume} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(volume)} Cubic meters more.')
