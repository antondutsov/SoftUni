# numerary = int(input())
# summary = 0
#
# for i in range(0, numerary):
#     current = int(input())
#     summary = summary + current
# print(summary)

numerary = int(input())
max_num = -1000000000000000


for i in range(numerary):
    num = int(input())
    if num > max_num:
        max_num = num
print(max_num)
