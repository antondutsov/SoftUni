fruit = input()
dayweek = input()
amount = float(input())

if dayweek == 'Saturday' or dayweek == 'Sunday':
    banana = 2.70
    apple = 1.25
    orange = 0.90
    grapefruit = 1.60
    kiwi = 3.00
    pineapple = 5.60
    grapes = 4.20
else:
    banana = 2.50
    apple = 1.20
    orange = 0.85
    grapefruit = 1.45
    kiwi = 2.70
    pineapple = 5.50
    grapes = 3.85
    
if dayweek != 'Workday':
    if fruit == 'banana':
        print('%.2f' % (banana * amount))
    elif fruit == 'apple':
        print('%.2f' % (apple * amount))
    elif fruit == 'orange':
        print('%.2f' % (orange * amount))
    elif fruit == 'grapefruit':
        print('%.2f' % (grapefruit * amount))
    elif fruit == 'kiwi':
        print('%.2f' % (kiwi * amount))
    elif fruit == 'pineapple':
        print('%.2f' % (pineapple * amount))
    elif fruit == 'grapes':
        print('%.2f' % (grapes * amount))
    else:
        print('error')    
else:
    print('error')
