# every day patients visits the 7 MDs
# every md can treat only 1 patient
# if patients are more than 7 they are untreated
# every three days if the untreated patients > treated add MD

work_days = int(input())  # period

treated_patients = 0
untreated_patients = 0
doctors_count = 7  # count_of_doctors

for day in range(1, work_days+1):
    patients_count = int(input())  # current_patients
    if (day % 3 == 0) and (untreated_patients > treated_patients):
        doctors_count += 1

    if patients_count > doctors_count:
        treated_patients += doctors_count
        untreated_patients += patients_count - doctors_count
    else:
        treated_patients += patients_count

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
