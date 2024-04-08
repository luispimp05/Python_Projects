from art import logo
from random import randint

# Global variables to use in turns
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#choose the difficulty level
def set_difficulty():
    level = input("Chose a difficulty: Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
        
    else : 
        return HARD_LEVEL_TURNS

   


#function to check the user's guess against the actual number
def check_answer(guess, answer, turns):
    """verifying the number of turns and if its wrong subtract one"""
    if guess > answer:
        print("Too High")
        return turns -1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer} .")
        
        
        
def game (): 
    print(logo)       
    print("Welcome to the Number Guessing Game!")
    print("Im thinking of a number between 1 and 100.")

#automatic random answer
    answer = randint(1, 100)
    print(f"The right number is {answer}")
#repeat he guessing functionally if they get it wrong. loopping
    turns = set_difficulty() 
    guess = 0  # make it global inside the function
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number. ")
        #user guess a number
        guess = int(input("Make a guess: "))#make it local inside the loop
        #check answer function call
        turns = check_answer(guess, answer, turns)
        
        # gets out of loop if you run out of guesses
        if turns == 0:
            print("you run out of guesses, you lose!")
            return
        elif guess != answer:
            print("Guess Again!")







 
# make a function to set difficulty



game()
