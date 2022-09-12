name = input()

failed = 0
grade = 1
gpa = 0

while True:
    grades = float(input())
    if 2 <= grades < 4.00:
        failed += 1
    else:
        if 4.00 <= grades <= 6.00:
            gpa += grades
            grade += 1
            
    if grade > 12:
        average_grade = gpa / 12
        print(f'{name} graduated. Average grade: {average_grade:.2f}')
        break

    if failed > 1:
        print(f'{name} has been excluded at {grade} grade')
        break
    