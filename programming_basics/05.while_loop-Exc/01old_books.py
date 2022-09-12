fav_book = input()

book = input()
searched = 0

while book != 'No More Books':
    if book == fav_book:
        print(f'You checked {searched} books and found it.')
        break
    book = input()
    searched += 1
else:
    print(f'The book you search is not here!\nYou checked {searched} books.')