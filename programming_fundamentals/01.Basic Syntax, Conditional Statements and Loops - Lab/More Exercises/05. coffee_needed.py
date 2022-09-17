events = ['coding', 'dog', 'cat', 'movie', 'CODING', 'DOG', 'CAT', 'MOVIE']
counter = 0

while True:
    event = input()
    if event == 'END':
        print(counter)
        break
    if event.isupper() and (event in events):
        counter += 2
    if event.islower() and (event in events):
        counter += 1
    if counter > 5:
        print('You need extra sleep')
        break
