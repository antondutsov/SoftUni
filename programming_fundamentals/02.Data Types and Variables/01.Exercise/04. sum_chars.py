words = int(input())
char_sum = 0

for i in range(words):
    word = input()
    char_sum += ord(word)
print('The sum equals: {}'.format(char_sum))
