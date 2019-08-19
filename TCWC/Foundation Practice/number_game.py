import random
import winsound

frequency=1000
duration=500

# Create the secret number #

rand_num=random.randint(1,100)

# I initialize some variables I will use later #
check=0

i=1 

# I will loop the code below as long as the number is correctly guessed and I will change the "check" variable value from 0 to 1 #
while check != 1:
    print(" ")
    print("Guess the number (between 0 and 100):")
    guess=input()

    try:

        if int(guess)==rand_num:
            check=1
        else:
            check=0

    except ValueError:
        print("Sorry, you can only enter values. you have lost")
        quit()

    i=i+1

    if int(guess)>rand_num:
        print("Guess less")
    if int(guess)<rand_num:
        print("Guess higher")

    
    winsound.Beep(frequency,duration)


print("YOU WON!!!! You guessed it in ",i,'Moves' )
   