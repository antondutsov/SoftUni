climbing_groups = int(input())

musala = 0
montblanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for i in range(climbing_groups):
    persons = int(input())
    if 5 >= persons:
        musala += persons
    elif 6 <= persons <= 12:
        montblanc += persons
    elif 13 <= persons <= 25:
        kilimanjaro += persons
    elif 26 <= persons <= 40:
        k2 += persons
    else:
        everest += persons
total = musala + montblanc + kilimanjaro + k2 + everest

print("{0:.2f}%".format(musala / total * 100))
print("{0:.2f}%".format(montblanc / total * 100))
print("{0:.2f}%".format(kilimanjaro / total * 100))
print("{0:.2f}%".format(k2 / total * 100))
print("{0:.2f}%".format(everest / total * 100))
