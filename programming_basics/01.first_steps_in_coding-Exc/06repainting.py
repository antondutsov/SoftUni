cover_nylon = (int(input()) + 2) * 1.50
paint = (float(input()) * 1.10) * 14.50
diluent = int(input()) * 5.00 + 0.4
shift_hours = int(input())
materials = cover_nylon + paint + diluent

work_force = (materials * 0.30) * shift_hours
total = work_force + materials
print(total)
