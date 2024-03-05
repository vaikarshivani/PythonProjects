import random

def play():
    while True:
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors, or 'q' to quit\n")
        
        if user == 'q':
            print("Goodbye!")
            break  # exit the loop if the user wants to quit
        
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            print('It\'s a tie')
        elif is_win(user, computer):
            print('You won!')
            break  # exit the loop if the user wins
        else:
            print('You lost! Try again.')

def is_win(player, opponent):
    # return true if player wins
    # r>s, s>p, p>r
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

# Run the game
play()
