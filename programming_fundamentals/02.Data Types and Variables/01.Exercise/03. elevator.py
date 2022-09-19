persons = int(input())
capacity = int(input())
courses = 0

while persons > 0:
    course = persons / capacity
    persons -= capacity
    courses += 1
print(courses)
