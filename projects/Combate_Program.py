# JQ 1st Combate Program
import time 
import random
health = 0
defense = 0
attack = 0
damage = 0
monster_health = 30
monster_defense = 13
monster_damage = 12
def monster_turn(x,y):
    strike = random.randint(1,20)
    if strike >= defense:
       return random.randint(1,12)
    else:
        return 0

        



print("Welcome to training! First I need to know some things about you!")
useless_info = input("What is your name that i will not be using?\n")
class_type = int(input("what class of fighter are you? \n1 if you are a Fighter \n2 if you are a Mage \n3 if you are a Rouge\n"))
if class_type == 1:
    print("your stats: \n Health: 30 \n Defense: 14 \n Attack: D20 + 3 \n Damage: D8 +4 ")
    health = 30
    defense = 14
    damage = 12
elif class_type == 1:
    print("your stats: \n Health: 15 \n Defense: 9 \n Attack: D20 + 6 \n Damage: D12 +4 ")
    health = 15
    defense = 9
    damage = 12
elif class_type == 1:
    print("your stats: \n Health: 20 \n Defense: 16 \n Attack: D20  \n Damage: D8 +4 ")
    health = 20
    defense = 16
    damage = 8
else: 
    print("there was an error, please try again")

turn = random.randint(1,2)
while monster_health > 0 or health > 0:
    if turn == 1:
        print(f"your stats: \n {health}/30 \n {defense} \n Attack: D20 + 3 \n Damage: D8 +4 ")
        action = input("its your turn, what is your action Attack\n Heal\n Flee\n protect\n").strip().lower()
        if action == "heal":
            health += random.randint(1,8)
            print(f"your health is now {health} hp" )
        elif action == "flee":
            chance = random.randint(1,2)
            if chance == 2:
                break
            elif chance == 1:
                print("you did not escape")
        elif:

    elif turn == 2:
        print ("its the monsters turn!")
        attack = random.randint(1,20)
        time.sleep(5)
        health -= monster_turn(health,defense)
        print(f"you have {health} hp remaining")

#heal
#attack
#@Flee
#rotect
