actor_name = input()
academy_points = float(input())
judges = int(input())

base = 1250.5

for committee in range(judges):
    judges_name = input()
    judges_points = float(input())
    academy_points += ((len(judges_name) * judges_points) / 2)
    if academy_points > base:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
        break
if academy_points < base:
    diff = base - academy_points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
