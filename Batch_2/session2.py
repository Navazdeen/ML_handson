# If else

"""
if condtion:
    code
elif condtion:
    code
else:
    code

age - 

1- 12 ->  teens
12-20 -> adults
20-40 -> Men/women
> 40 - senior citizen

# Logical Operators
and or 

"""
player1="rock"
player2="scissor"

if player1 == player2:
    print("draw")
elif player1 == "rock" and player2 == "paper":
    print("player2 Win's")
elif player1 =="rock" and player2 == "scissor":
    print("player1 Win's")
elif player1 == "paper" and player2 == "rock":
    print("player1 Win's")
elif player1 == "paper" and player2 == "scissor":
    print("player2 Win's")
elif player1 == "scissor" and player2 =="rock":
    print("player2 Win's")
elif player1 == "scissor" and player2 =="paper":
    print("player1 Win's")

