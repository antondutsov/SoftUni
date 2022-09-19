lines = int(input())

flag = False
open_bracket = 0
closing_bracket = 0

for line in range(lines):
    word = input()
    if word == '(':
        open_bracket += 1
    if word == ')':
        closing_bracket += 1

if closing_bracket == open_bracket:
    flag = True

if flag:
    print('BALANCED')
else:
    print('UNBALANCED')
