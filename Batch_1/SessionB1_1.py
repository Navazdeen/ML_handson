"""
age < 12 -> children
12 < age < 20 -> Teen
20 < age < 30 -> Men/Women
30 < age < 50 -> Senior citizen
"""

# age = 20

# if age <= 12:
#     print("Children")
# elif 12 < age <= 20:
#     print("Teen")
# elif 20 < age <= 30:
#     print("Men/Women")
# elif 30 < age <= 50:
#     print("Senior Citizen")
# else:
#     print("Grand senior citizen")

# player1 = "paper"
# player2 = "scissor"

# if player1 == player2:
#     print("Draw")
# elif player1 == "rock" and player2=="paper":
#     print("player2 Win's")
# elif player1=="rock" and player2=="scissor":
#     print("player1 Win's")
# elif player1=="paper" and player2=="scissor":
#     print("player2 Win's")
# elif player1=="paper" and player2=="rock":
#     print("player1 Win's")
# elif player1=="scissor" and player2=="rock":
#     print("player2 Win's")
# elif player1 == "scissor" and player2=="paper":
#     print("player1 Win's")

# range -> range(start, stop, step)

lst = [1, 2, 3, 4, 5]

# for var_name in lst:
    # code

# print(lst[0])
# print(lst[1])
# print(lst[2])
# print(lst[3])
# print(lst[4])

# for item in range(1, 20):
#     print(item)

# 1 is odd
# 2 is even
# 3 is odd

# 24 % 2 == 0

for num in range(1, 100):
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")


# Any number / 10
# Any number % 10