count = int(input())

last_pair, cur_pair, diff = 0, 0, 0

# first pair
for i in range(2):
    n = int(input())
    last_pair += n

if count == 1:
    print(f'Yes, value={last_pair}')

else:
    for i in range(count - 1):
        a = int(input())
        b = int(input())
        cur_pair = a + b

        if cur_pair != last_pair:
            diff = abs(cur_pair - last_pair)

        last_pair = cur_pair

    if diff:
        print(f'No, maxdiff={diff}')
    else:
        print(f'Yes, value={last_pair}')

