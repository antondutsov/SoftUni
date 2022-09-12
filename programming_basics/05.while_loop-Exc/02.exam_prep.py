failed_grades = int(input())

failed_counter = 0
subject_counter = 0
grade_sum = 0
subject_name = ''
subject = ''
while failed_counter < failed_grades:
    subject_name = subject
    subject = input()
    if subject == 'Enough':
        average_score = grade_sum / subject_counter
        print(f'Average score: {average_score:.2f}')
        print(f'Number of problems: {subject_counter}')
        print(f'Last problem: {subject_name}')
        break
    grade = int(input())
    grade_sum += grade
    subject_counter += 1
    if grade <= 4:
        failed_counter += 1
else:
    print(f'You need a break, {failed_counter} poor grades.')
