# SQUARE
# RECTANGLE
# CIRCLE
# TRIANGLE

figure = input()

if figure == "square" or figure == "SQUARE":
    a = float(input())
    square = a * a
    print(f"{square:.3f}")
elif figure == "rectangle" or figure == "RECTANGLE":
    a = float(input())
    b = float(input())
    rectangle = a * b
    print(f"{rectangle:.3f}")
elif figure == "circle" or figure == "CIRCLE":
    a = float(input())
    circle = 3.14159 * (a * a)
    print(f"{circle:.3f}")
elif figure == "triangle" or figure == "TRIANGLE":
    a = float(input())
    b = float(input())
    area = (b * a) / 2
    print(f"{area:.3f}")
else:
    print("Enter figure:\n \"SQUARE\"; \"RECTANGLE\"; \"CIRCLE\"; \"TRIANGLE\"")
