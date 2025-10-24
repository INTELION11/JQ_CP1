# JQ 1st Combate Program
import time 
import random

def monster_turn(strike):
    if strike >=


print("Welcome to training! First I need to know some things about you!")
useless_info = input("What is your name that i will not be using?\n")
class_type = int(input("what class of fighter are you? \n1 if you are a Fighter \n2 if you are a Mage \n3 if you are a Rouge\n"))
if class_type == 1:
    print("your stats: \n Health: 30 \n Defense: 14 \n Attack: D20 + 3 \n Damage: D8 +4 ")
elif class_type == 1:
    print("your stats: \n Health: 15 \n Defense: 9 \n Attack: D20 + 6 \n Damage: D12 +4 ")
elif class_type == 1:
    print("your stats: \n Health: 20 \n Defense: 16 \n Attack: D20  \n Damage: D8 +4 ")
else: 
    print("there was an error, please try again")

turn = random.randint(1,2)

if turn == 1:
   action = input("its your turn, what is your action Attack\n Heal\n Flee\n protect\n").strip().lower()

elif turn == 2:
    print ("its the monsters turn!")
    time.sleep(5)
    monster_turn("attack")

#heal
#attack
#@Flee
#rotect
