#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   Conditionals - Life of Brian guessing game using a while True loop."""

def main():

    # Initialize counter
    round = 0

    #increment counter
    while True:
        round = round + 1
        
        print('Finish the movie title, "Monty Python\'s The Life of ______"')
        
        #User input answer
        answer = input("Your guess--> ")
        
        #test conditional statement
        if answer == 'Brian':
            print ('Correct')
            break
        elif round==3:
            print("Sorry, the answer was Brian.")
            break
        else:
            print("Sorry! Try again!")

main()
