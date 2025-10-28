#JQ 1st Combate Program
import time  
import random  
  
health = 0  
defense = 0  
attack = 0  
damage = 0  
monster_health = 30  
monster_defense = 13  
monster_damage = 12  
protect = False  
  
def monster_turn(player_health, player_defense):  
    strike = random.randint(1, 20)  
    if strike >= player_defense:  
        print("the monster hits you!")  
        return random.randint(1, 12)  
    else:  
        print("the monster missed!")  
        return 0  
  
def player_turn(health, defense, attack, damage, monster_health, monster_defense, protect):  
    print(f"your stats: \n {health} HP\n Defense: {defense}\n")  
    action = input("its your turn, what is your action \nAttack\n Heal\n Flee\n protect\n").strip().lower()  
    next_protect = False  
    result = {"health": health, "defense": defense, "monster_health": monster_health, "protect": False, "flee": False}  
    if action == "heal":  
        heal_amt = random.randint(1, 8)  
        result["health"] += heal_amt  
        print(f"you healed {heal_amt} points! your health is now {result['health']} hp")  
    elif action == "flee":  
        chance = random.randint(1, 2)  
        if chance == 2:  
            print("you got away! you live to fight another day!")  
            result["flee"] = True  
        else:  
            print("you did not escape")  
    elif action == "protect":  
        next_protect = True  
        print("you brace yourself for the next attack!")  
    elif action == "attack":  
        your_attack = random.randint(1, 20) + attack  
        print(f"you rolled a {your_attack} to hit!")  
        if your_attack >= monster_defense:  
            dmg = random.randint(1, damage) + 4  
            result["monster_health"] -= dmg  
            print(f"you hit the monster for {dmg} points! monster has {result['monster_health']} hp left")  
        else:  
            print("you missed!")  
    else:  
        print("not a valid action, try again!")  
        return player_turn(result["health"], result["defense"], attack, damage, result["monster_health"], monster_defense, next_protect)  
    result["protect"] = next_protect  
    return result  
  
print("Welcome to training! First I need to know some things about you!")  
useless_info = input("What is your name that i will not be using?\n")  
class_type = int(input("what class of fighter are you? \n1 if you are a Fighter \n2 if you are a Mage \n3 if you are a Rouge\n"))  
if class_type == 1:  
    print("your stats: \n Health: 30 \n Defense: 14 \n Attack: D20 + 3 \n Damage: D8 +4 ")  
    health = 30  
    defense = 14  
    attack = 3  
    damage = 8  
elif class_type == 2:  
    print("your stats: \n Health: 15 \n Defense: 9 \n Attack: D20 + 6 \n Damage: D12 +4 ")  
    health = 15  
    defense = 9  
    attack = 6  
    damage = 12  
elif class_type == 3:  
    print("your stats: \n Health: 20 \n Defense: 16 \n Attack: D20  \n Damage: D8 +4 ")  
    health = 20  
    defense = 16  
    attack = 0  
    damage = 8  
else:   
    print("there was an error, please try again")  
    exit()  
  
turn = random.randint(1, 2)  
  
while monster_health > 0 and health > 0:  
    if turn == 1:  
        result = player_turn(health, defense, attack, damage, monster_health, monster_defense, protect)  
        health = result["health"]  
        monster_health = result["monster_health"]  
        protect = result["protect"]  
        if result["flee"]:  
            break  
        turn = 2  
    elif turn == 2:  
        print("its the monsters turn!")  
        time.sleep(1)  
        temp_defense = defense  
        if protect:  
            temp_defense += 4  
            print("your defense is higher this turn because you are protecting!")  
        health -= monster_turn(health, temp_defense)  
        print(f"you have {health} hp remaining")  
        protect = False  
        turn = 1  
  
if health <= 0:  
    print("you have fallen in battle. try again next time!")  
elif monster_health <= 0:  
    print("you win! monster is defeated, that was too easy right?!")  