import sys
user1 = "Player 1"
user2 = "Player 2"
print("Enter your choice Rock, paper or scissor: \n")
user1_answer = input("%s :" % user1)
user2_answer = input("%s :" % user2)
def compare(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissor':
            return("Player 1 wins!")
        else:
            return("Player 2 wins!")
    elif u1 == 'scissor':
        if u2 == 'paper':
            return("Player 1 win!")
        else:
            return("Player 2 wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            return("Player 1 wins!")
        else:
            return("Player 2 win!")
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")
        sys.exit()
print(compare(user1_answer, user2_answer))