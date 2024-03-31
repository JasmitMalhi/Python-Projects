import random
#improted the random module

topRange=input("Type a number: ")
#Following checks if it is a number
if topRange.isdigit():
    topRange=int(topRange)
    if topRange <=0:
     print("Please type a number larger than 0 next time.")
     quit()
else:
    print("Please type a number next time")
    quit()
randomNum=random.randint(0,topRange)
print(randomNum)
      
while True:
    guesses=0
    guesses+=1
    userGuess= input("Make a guess: ")
    if userGuess.isdigit():
        userGuess=int(userGuess)
    else:
        print("Please type a number next time")
        continue


    if userGuess==randomNum:
        print("You got it!")
        break
    elif userGuess>randomNum:
        print("Too high")
    else:
        print("Too low")
print("you got it in",guesses, "guesses")

 # random.randrange(start,stop(uninclusive))
       # random.randrange(stop(0-stop))
       # random.randint(start,stop(inclusive))
#Continues the loop to keep going
#break breaks the loop

