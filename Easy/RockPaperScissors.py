import random
userWins=0
computerWins=0
options=["r","p","s"]
while True:
    userGuess=input("R/P/S/Q").lower()
    if userGuess=="q":
        break

    if userGuess not in options:
        continue#keeps going if not the write input
    random_number=random.randint(0,2)
    #rock:0, paper:1, scissors:2
    computerPick=options[random_number]
    print("Computer Picked", computerPick+".")

    if userGuess=="r" and computerPick=="s":
        print("you won!")
        userWins+=1
        continue

    elif userGuess=="p" and computerPick=="r":
        print("you won!")
        userWins+=1
        continue

    elif userGuess=="s" and computerPick=="p":
        print("you won!")
        userWins+=1
        continue
    else:
        print("Lost")
        computerWins+=1





print("you won", userWins)
print("Computer won", computerWins)

print("goodbye")
