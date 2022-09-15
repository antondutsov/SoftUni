# 5
# **********     **********
# *////////*     *////////*
# *////////*|||||*////////*
# *////////*     *////////*
# **********     **********


n = int(input())

    # print top part
print("*" * (2 * n), end="")
print(" " * n, end="")
print("*" * (2 * n))

    # print the middle part
for i in range(n - 2):
    pass
    # print the middle part


    # print bottom part
print("*" * (2 * n), end="")
print(" " * n, end="")
print("*" * (2 * n))

for i in range(n - 2):
    pass
    # print *////////*
    if i == (n - 1) // 2 - 1:
        print("|" * n, end="")
    else:
        print(" " * n, end="")
    # print *///////*
    print()
