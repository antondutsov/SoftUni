# On the first line, you will be given a positive number, which will serve
# as  a divisor. On the second line, you will receive a positive number
# that  will be the boundary. You should find the largest integer N, that is:

divisor = int(input())
boundary = int(input())

boundary -= (boundary % divisor)
print(boundary)
