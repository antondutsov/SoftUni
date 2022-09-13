floor_number = int(input())
room_number = int(input())

floor_letter = ''
for floor in range(floor_number, 0, -1):
    for room in range(room_number):
        if floor == floor_number:
            floor_letter = 'L'
        elif floor % 2 != 0:
            floor_letter = 'A'
        else:
            floor_letter = 'O'
        print(f'{floor_letter}{floor}{room}', end=' ')
    print()
