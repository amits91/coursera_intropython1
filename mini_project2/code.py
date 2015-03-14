# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# Import the module
import simplegui
import random
import math

num_range = 100
secret_number = 10
allowed_guess = 7
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, num_range, allowed_guess
    allowed_guess = int(math.ceil(math.log(num_range + 1, 2)))
    print 'New game. Range is 0 to', num_range
    print 'Number of remaining guess', allowed_guess
    secret_number = random.randrange(0, num_range)


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range = 1000
    new_game()
    
def input_guess(guess):
    gn = float(guess)
    print 'Guess was', gn
    global secret_number, allowed_guess
    allowed_guess = allowed_guess - 1
    print 'Number of remaining guess', allowed_guess
    if gn < secret_number:
        print 'Lower!'
    elif gn > secret_number:
        print 'Higher!'
    else:
        print 'Correct!'
    if (allowed_guess == 0):
        if (gn != secret_number):
            print 'You lose!'
        new_game()
    
# create frame
frame = simplegui.create_frame('Guess the Number', 200, 200)

# register event handlers for control elements and start frame
button1 = frame.add_button('Range is [0, 100)', range100)
button2 = frame.add_button('Range is [0, 1000)', range1000)
inp = frame.add_input('Enter a guess', input_guess, 100)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
