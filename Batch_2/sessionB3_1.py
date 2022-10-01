# FOR LOOP

# range --> range(start, stop, step)


# for var_name in lst:
#   code

# for item in range(0, 500):
#     print(item)


# 24 % 2 == 0

# for num in range(1, 100):
#     if num % 2 == 0:
#         print(num, "is even")
#     else:
#         print(num, "is odd")

# 144 % 10 ==> 4
# 144 / 10 ==> 14.4

number = 3375
digit = 4

# 5
# 7
# 3
# 3

# for _ in range(0, digit):
#     rem = number % 10
#     print(rem)
#     number = int(number/10)

# number = 3421
# digit = 4

# for _ in range(0, digit):
#     rem = number % 10 
#     print(rem ** 2)
#     number = int(number/10)

"""OUTPUT = 
1
4
16
9
"""
# N = 10
# sum = 0 
# for num in range(1, N+1):
#     sum = sum + num


# print(sum)

# N = 4
# sum = 0 
# for num in range(1, N+1):
#     sum = sum + (num**2)

# print(sum)
N=8

for i in range(1, 11):  #1*4 = 4
    print(i, "x", N, "=", i*N)

