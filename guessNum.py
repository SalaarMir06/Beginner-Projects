# Best wishes mates
import random
import time

start = int(input("Enter the range start: "))
stop = int(input("Enter the range ending point: "))
def guess():
    randomNumber = random.randint(start,stop) #randint is used for generating random integer
    tries = 0

    # using while loop to iterate it x number of times
    while guess !=randomNumber:
        guessNum = int(input("Enter a random number:   "))
        tries = tries + 1
        
        # identifying the stage of number
        if guessNum>randomNumber:
            print("Sorry mate, guess's quite high")
        elif guessNum<randomNumber:
            print("Sorry mate, guess's quite low")
        else:
            print("Cool😎 you guessed it. Well let's see how many tries did you take:")
            break #break statement is to break out of loop

    print("Calculating")

    # time.sleep(x) can be used to add delay where x represents n seconds
    time.sleep(2)

    print(f"you took \033[1;32m{tries}\033[0m tries to guess the correct number.")
    # \033[1;32m: This is the escape sequence to apply bold (1) and green color (32) to the text.

    # 1: Bold text
    # 32: Green text color

# \033[0m: This resets the formatting back to normal, ensuring that subsequent text is not affected by the style.

guess()
