width = int(input())
length = int(input())

area = width * length
total_pieces = area / 1

guests = 0
command = ''

while command != 'stop' and total_pieces > 0:
    command = input().lower()
    if command.isnumeric():
        total_pieces -= int(command)
    else:
        break

if total_pieces > 0:
    print('%d pieces are left.' % total_pieces)
else:
    print('No more cake left! You need %d pieces more.' % abs(total_pieces))