# JQ 1st Rock Paper Scissor
import random
while True:
    choice = input(" press q to quit, Lets play Rock paper scissors, Rock Paper Scissors Shoot!! \n").lower().strip()
    npc = random.randint(1,3)
    if choice == "rock":
        if npc == 1:
            print("rock!!")
            print(" We tied!!")
        elif  npc == 2:
            print("Paper!!")
            print(" You loose ")
        elif npc == 3:
            print("scissors!!")
            print(" You win")
        else:
            print(" Please try again ")
    elif choice == "paper":
        if npc == 1:
            print("rock!!")
            print(" you win ")
        elif  npc == 2:
            print("Paper!!")
            print(" We tied ")
        elif npc == 3:
            print("scissors!!")
            print(" You loose ")
        else:
            print(" Please try again ")
    elif choice == "scissors":
        if npc == 1:
            print("rock!!")
            print(" You Loose ")
        elif  npc == 2:
            print("Paper!!")
            print(" You win ")
        elif npc == 3:
            print("scissors!!")
            print(" We tied ")
        else:
            print(" Please try again ")
    elif choice == "q":
        break
    else:
        print("Invalid input, try rock, paper, scissors")

        