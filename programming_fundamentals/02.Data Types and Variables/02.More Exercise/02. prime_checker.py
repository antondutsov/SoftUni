num = int(input())

flag = False

if num > 1:
    for n in range(2, num):
        if (num % n) == 0:
            flag = True
            break
if flag:
    print('False')
else:
    print('True')
