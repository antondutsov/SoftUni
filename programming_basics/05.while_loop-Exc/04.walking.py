goal = 10000
steps = 0

while True:
    command = input()
    if command.isnumeric():
        steps += int(command)
        if steps >= goal:
            break
        continue
    else:
        steps += int(input())
        break

if steps >= goal:
    print('Goal reached! Good job!')
    if steps > goal:
        print(f'{steps - goal} steps over the goal!')
else:
    print(f'{goal - steps} more steps to reach goal.')