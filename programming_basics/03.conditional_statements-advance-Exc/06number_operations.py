n1 = int(input())
n2 = int(input())
operator = input()

result = 0
remainder = 0
even_odd = ""

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        result = n1 + n2
    if operator == "-":
        result = n1 - n2
    if operator == "*":
        result = n1 * n2
    if result % 2 == 0:
        even_odd = "even"
    if result % 2 != 0:
        even_odd = "odd"
    print(f"{n1} {operator} {n2} = {result} - {even_odd}")
elif operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} {operator} {n2} = {result:.2f}")
elif operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} {operator} {n2} = {result}")
else:
    print("Enter valid operator!")
