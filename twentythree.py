# write a program for a simple countdown timer using a while loop

timerLimit = int(input("Enter the timer limit: "))

while timerLimit >= 1:
    print(f"{timerLimit} seconds")
    timerLimit -= 1

print("Time's up!")