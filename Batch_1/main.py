"""
if condition:
    if condition:
        `code`
    else:
        `code`
elif condition:
    if condtion:
        code
    else:
        code
else:
    code
"""

player1="rock"
player2="scissor"


"""
if 
elif
elif
elif
else
"""


if player1 == player2:
    print("Draw")
elif player1 == "rock":
    if player2 == "paper":
        print("player2 win's")
    elif player2 == "scissor":
        print("player1 win's")
elif player1 == "paper":
    if player2 == "rock":
        print("playerr1 Win's")
    elif player2 == "scissor":
        print("player2 Win's")
elif player1 == "scissor":
    if player2 == "rock":
        print("player2 Win's")
    elif player2 == "paper":
        print("player1 Win's")

