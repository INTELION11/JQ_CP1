import random as r  
import time as t  
import sys  
  
def sprint(text, delay=0.025):  
    for char in text:  
        sys.stdout.write(char)  
        sys.stdout.flush()  
        t.sleep(delay)  
    print()  
  
# Inventory as a dictionary (item: damage)  
inventory = {  
    "greatsword": 12,
    "fist": 4,
    "wotter bhottle": "heal10"
}  
  
# Welcome message (light grey text)  
sprint("\033[37mWelcome, Lyte! Prepare for your journey... \033[0m")  
  
# Randomly assign player stats  
player_str = r.randint(1, 20)  
player_dex = r.randint(1, 20)  
player_hp = r.randint(60, 70)  
player_ac = r.randint(9, 11)  
  
# Show player stats  
sprint(f"Your stats:\n  STR: {player_str}\n  DEX: {player_dex}\n  HP: {player_hp}\n  AC: {player_ac}")  
  
# Offer reroll  
action = input("You have one more chance to reroll. Say yes to reroll, no to continue: ").strip().lower()  
if action == "yes":  
    player_str = r.randint(1, 20)  
    player_dex = r.randint(1, 20)  
    player_hp = r.randint(60, 70)  
    player_ac = r.randint(9, 11)  
    sprint(f"Your new stats:\n  STR: {player_str}\n  DEX: {player_dex}\n  HP: {player_hp}\n  AC: {player_ac}")  
elif action == "chupacabra":  # Dev Secret code  
    player_str = 999999999999  
    player_dex = 999999999999  
    player_hp = 1  
    player_ac = 999999999999  
    sprint(f"Dev mode!\n  STR: {player_str}\n  DEX: {player_dex}\n  HP: {player_hp}\n  AC: {player_ac}")  
player_gold = 0
player_exhaustion = 0
maximum_player_health = player_hp
# Cutscene intro  
sprint("Lyte meets Cronos. Cronos throws him away...")  
  

def combat(player_hp, player_str, player_ac, player_dex, monster_hp, monster_ac, monster_dmg, inventory, player_exhaustion):  
    turn = r.randint(1,2)  
    exhaustion_penalty = player_exhaustion 
    while player_hp > 0 and monster_hp > 0:  
        if turn == 1:  
            player_exhaustion += .5
            sprint(f"\nYour stats: {player_hp} HP | AC: {player_ac} | Exhaustion: {player_exhaustion}")  
            action = input("Do you want to 'attack' or 'heal'? ").strip().lower()  
            sprint("Inventory: " + ", ".join(inventory.keys()))  
            item = input("Which item do you want to use? ").strip().lower()  
            if item not in inventory:  
                sprint("That item is not in your inventory.")  
                continue  
            
            if action == "heal" and str(inventory[item]).startswith("heal"):  
                max_heal = int(str(inventory[item])[4:])  
                heal_amt = r.randint(1, max_heal)  
                player_hp += heal_amt  
                sprint(f"You used {item}, healed {heal_amt} HP! Now at {player_hp} HP.")  
             
            elif action == "attack" and type(inventory[item]) == int:  
                to_hit = r.randint(1, 20) + player_str // 4 - exhaustion_penalty  
                sprint(f"You rolled a {to_hit} to hit!")  
                if to_hit >= monster_ac:  
                    dmg = max(1, r.randint(1, inventory[item]) + player_str // 4 - exhaustion_penalty)  
                    monster_hp -= dmg  
                    sprint(f"You hit for {dmg} damage! Monster has {monster_hp} HP left.")  
                else:  
                    sprint("You missed!")  
            else:  
                sprint(f"You can't do that with {item}.")  
                continue  
            turn = 2  
        else:  
            sprint("Monster's turn!")  
            t.sleep(1)  
            to_hit = r.randint(1, 20)  
            if to_hit >= player_ac + player_dex // 4:  
                dmg = r.randint(1, monster_dmg)  
                player_hp -= dmg  
                sprint(f"The monster hits you for {dmg} damage! You now have {player_hp} HP.")  
            else:  
                sprint("The monster missed!")  
            turn = 1  
  
    if player_hp <= 0:  
        sprint("Try again next time!")  
        return 'lose', player_hp, player_str, player_dex, player_ac, player_exhaustion  
    elif monster_hp <= 0:  
        sprint("You win! Monster defeated!")  
        return 'win', player_hp, player_str, player_dex, player_ac, player_exhaustion  

  
def desert_hammurabi(player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion,maximum_player_health):  
    sprint("\033[38;5;223mA hot wind blows. You stand in the desert as a monster appears\033[0m")  
    monster_hp = 30  
    monster_ac = 13  
    monster_dmg = 12  
    result, player_hp, player_str, player_dex, player_ac, player_exhaustion = combat(  
        player_hp, player_str, player_ac, player_dex, monster_hp, monster_ac, monster_dmg, inventory, player_exhaustion  
    )  
    if result == 'win':  
        loot = r.choice(['gold', 'meat', 'stat',"health"])  
        if loot == 'gold':  
            player_gold += 5  
            sprint("you found 5 gold coin!")  
        elif loot == 'stat':  
            sprint("You found an ancient relic! Choose a stat to increase: STR, DEX, or AC.")  
            stat = input("Which stat do you want to increase? ").strip().lower()  
            if stat == 'str':  
                player_str += 1  
                sprint("Your STR increased by 1!")  
            elif stat == 'dex':  
                player_dex += 1  
                sprint("Your DEX increased by 1!")  
            elif stat == 'ac':  
                player_ac += 1  
                sprint("Your AC increased by 1!")  
            else:  
                sprint("Invalid choice. No stat increased.") 
        elif loot == "health":
            maximum_player_health += r.randint(1,5)
            sprint(f"Your HP stat increased, it is now {maximum_player_health}")
    player_hp = maximum_player_health; cristal += 1

desert_hammurabi(player_hp, player_dex, player_str, player_ac, inventory,player_gold, player_exhaustion,maximum_player_health)
def The_iztec_Jungla(player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion,maximum_player_health):  
    sprint("\033[38;5;223mA hot wind blows. You stand in the desert as a monster appears\033[0m")  
    monster_hp = 30  
    monster_ac = 13  
    monster_dmg = 12  
    result, player_hp, player_str, player_dex, player_ac, player_exhaustion = combat(  
        player_hp, player_str, player_ac, player_dex, monster_hp, monster_ac, monster_dmg, inventory, player_exhaustion  
    )  
    if result == 'win':  
        loot = r.choice(['gold', 'meat', 'stat',"health"])  
        if loot == 'gold':  
            player_gold += 5  
            sprint("You found 5 gold coin!")  
        elif loot == 'stat':  
            sprint("You found an ancient relic! Choose a stat to increase: STR, DEX, or AC.")  
            stat = input("Which stat do you want to increase? ").strip().lower()  
            if stat == 'str':  
                player_str += 1  
                sprint("Your STR increased by 1!")  
            elif stat == 'dex':  
                player_dex += 1  
                sprint("Your DEX increased by 1!")  
            elif stat == 'ac':  
                player_ac += 1  
                sprint("Your AC increased by 1!")  
            else:  
                sprint("Invalid choice. No stat increased.") 
        elif loot == "health":
            maximum_player_health += r.randint(1-5)
            sprint(f"Your HP stat increased, it is now {maximum_player_health}")
    inventory["dagger"] = 10
    player_hp = maximum_player_health; cristal += 1
def TheWarpedrealm(player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion,maximum_player_health):  
    sprint("\033[38;5;223mA hot wind blows. You stand in the desert as a monster appears\033[0m")  
    monster_hp = 30  
    monster_ac = 13  
    monster_dmg = 12  
    result, player_hp, player_str, player_dex, player_ac, player_exhaustion = combat(  
        player_hp, player_str, player_ac, player_dex, monster_hp, monster_ac, monster_dmg, inventory, player_exhaustion  
    )  
    if result == 'win':  
        loot = r.choice(['gold', 'meat', 'stat',"health"])  
        if loot == 'gold':  
            player_gold += 5  
            sprint("you found 5 gold coin!")  
        elif loot == 'stat':  
            sprint("You found an ancient relic! Choose a stat to increase: STR, DEX, or AC.")  
            stat = input("Which stat do you want to increase? ").strip().lower()  
            if stat == 'str':  
                player_str += 1  
                sprint("Your STR increased by 1!")  
            elif stat == 'dex':  
                player_dex += 1  
                sprint("Your DEX increased by 1!")  
            elif stat == 'ac':  
                player_ac += 1  
                sprint("Your AC increased by 1!")  
            else:  
                sprint("Invalid choice. No stat increased.") 
        elif loot == "health":
            maximum_player_health += r.randint(1-5)
            sprint(f"Your HP stat increased, it is now {maximum_player_health}")
    player_hp = maximum_player_health; cristal += 1
def Pangeon(player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion,maximum_player_health):  
    sprint("\033[38;5;223mA hot wind blows. You stand in the desert as a monster appears\033[0m")  
    monster_hp = 30  
    monster_ac = 13  
    monster_dmg = 12  
    result, player_hp, player_str, player_dex, player_ac, player_exhaustion = combat(  
        player_hp, player_str, player_ac, player_dex, monster_hp, monster_ac, monster_dmg, inventory, player_exhaustion  
    )  
    if result == 'win':  
        loot = r.choice(['gold', 'meat', 'stat',"health"])  
        if loot == 'gold':  
            player_gold += 5  
            sprint("you found 5 gold coin!")  
        elif loot == 'stat':  
            sprint("You found an ancient relic! Choose a stat to increase: STR, DEX, or AC.")  
            stat = input("Which stat do you want to increase? ").strip().lower()  
            if stat == 'str':  
                player_str += 1  
                sprint("Your STR increased by 1!")  
            elif stat == 'dex':  
                player_dex += 1  
                sprint("Your DEX increased by 1!")  
            elif stat == 'ac':  
                player_ac += 1  
                sprint("Your AC increased by 1!")  
            else:  
                sprint("Invalid choice. No stat increased.") 
        elif loot == "health":
            maximum_player_health += r.randint(1-5)
            sprint(f"Your HP stat increased, it is now {maximum_player_health}")
    player_hp = maximum_player_health; cristal += 1
def Modern_world(player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion,maximum_player_health):  
    sprint("\033[38;5;223mA hot wind blows. You stand in the desert as a monster appears\033[0m")  
    monster_hp = 30  
    monster_ac = 13  
    monster_dmg = 12  
    result, player_hp, player_str, player_dex, player_ac, player_exhaustion = combat(  
        player_hp, player_str, player_ac, player_dex, monster_hp, monster_ac, monster_dmg, inventory, player_exhaustion  
    )  
    if result == 'win':  
        loot = r.choice(['gold', 'meat', 'stat',"health"])  
        if loot == 'gold':  
            player_gold += 5  
            sprint("you found 5 gold coin!")  
        elif loot == 'stat':  
            sprint("You found an ancient relic! Choose a stat to increase: STR, DEX, or AC.")  
            stat = input("Which stat do you want to increase? ").strip().lower()  
            if stat == 'str':  
                player_str += 1  
                sprint("Your STR increased by 1!")  
            elif stat == 'dex':  
                player_dex += 1  
                sprint("Your DEX increased by 1!")  
            elif stat == 'ac':  
                player_ac += 1  
                sprint("Your AC increased by 1!")  
            else:  
                sprint("Invalid choice. No stat increased.") 
        elif loot == "health":
            maximum_player_health += r.randint(1-5)
            sprint(f"Your HP stat increased, it is now {maximum_player_health}")
    player_hp = maximum_player_health; cristal += 1
def Cybercity_3012(player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion,maximum_player_health):  
    sprint("\033[38;5;223mA hot wind blows. You stand in the desert as a monster appears\033[0m")  
    monster_hp = 30  
    monster_ac = 13  
    monster_dmg = 12  
    result, player_hp, player_str, player_dex, player_ac, player_exhaustion = combat(  
        player_hp, player_str, player_ac, player_dex, monster_hp, monster_ac, monster_dmg, inventory, player_exhaustion  
    )  
    if result == 'win':  
        loot = r.choice(['gold', 'meat', 'stat',"health"])  
        if loot == 'gold':  
            player_gold += 5  
            sprint("you found 5 gold coin!")  
        elif loot == 'stat':  
            sprint("You found an ancient relic! Choose a stat to increase: STR, DEX, or AC.")  
            stat = input("Which stat do you want to increase? ").strip().lower()  
            if stat == 'str':  
                player_str += 1  
                sprint("Your STR increased by 1!")  
            elif stat == 'dex':  
                player_dex += 1  
                sprint("Your DEX increased by 1!")  
            elif stat == 'ac':  
                player_ac += 1  
                sprint("Your AC increased by 1!")  
            else:  
                sprint("Invalid choice. No stat increased.") 
        elif loot == "health":
            maximum_player_health += r.randint(1-5)
            sprint(f"Your HP stat increased, it is now {maximum_player_health}")
    player_hp = maximum_player_health; cristal += 1
def Medieval_Europe(player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion,maximum_player_health):  
    sprint("\033[38;5;223mA hot wind blows. You stand in the desert as a monster appears\033[0m")  
    monster_hp = 30  
    monster_ac = 13  
    monster_dmg = 12  
    result, player_hp, player_str, player_dex, player_ac, player_exhaustion = combat(  
        player_hp, player_str, player_ac, player_dex, monster_hp, monster_ac, monster_dmg, inventory, player_exhaustion  
    )  
    if result == 'win':  
        loot = r.choice(['gold', 'meat', 'stat',"health"])  
        if loot == 'gold':  
            player_gold += 5  
            sprint("you found 5 gold coin!")  
        elif loot == 'stat':  
            sprint("You found an ancient relic! Choose a stat to increase: STR, DEX, or AC.")  
            stat = input("Which stat do you want to increase? ").strip().lower()  
            if stat == 'str':  
                player_str += 1  
                sprint("Your STR increased by 1!")  
            elif stat == 'dex':  
                player_dex += 1  
                sprint("Your DEX increased by 1!")  
            elif stat == 'ac':  
                player_ac += 1  
                sprint("Your AC increased by 1!")  
            else:  
                sprint("Invalid choice. No stat increased.") 
        elif loot == "health":
            maximum_player_health += r.randint(1-5)
            sprint(f"Your HP stat increased, it is now {maximum_player_health}")
    player_hp = maximum_player_health; cristal += 1


 

# For each world, do the following:  
    # Show a cutscene with a description of the place  
    # Set up the monster: example: mon_hp = 34, mon_dex = 13, mon_weapon = "body"  
    # Start combat: player and monster fight until one is dead  
        # Player can use anything in their inventory (weapons, armor, etc)  
        # Weapons and armor change how easy it is to hit or dodge  
    # Some worlds have special rules:  
        # Desert: lose stamina faster (exhaustion)  
        # Cybercity: fight multiple monsters, -4 dexterity for player  
        # Pangeon: every 2 turns, player takes oxygen poisoning damage (1d4)  
        # Warpedrealm: +4 DEX for player  
        # Modern world: player is intimidated (has disadvantage) and -4 STR  
    # If the monster is dead:  
        # Add rewards to the inventory (could be meat, gold, time_cristal, or special artifact depending on the map)  
        # Show the updated inventory  
        # Open the shopkeeper, show dialogue, show items to buy, exit shop  
    # If the player is dead:  
        # Restart the game from the beginning  
  
"""-------------------------------------------------------------------------------------------------------------------------------"""  
# Define the Final Boss (Cronos)  
    # Show Cronos's dialogue  
    # Start combat with Cronos: he can attack 6 times at once (hexaweilder)  
    # For every world you have been to, Cronos loses one of his arms and one attack/turn  
    # If you defeat him, show a victory message and ask if you want to restart  
    # If you lose, show a sad message and ask if you want to restart  
  
"""-------------------------------------------------------------------------------------------------------------------------------"""  
# Define the Ötzi’s Tusdra Minigame  
    # Show intro dialogue for the minigame  
    # Start a stopwatch, show items one by one  
    # Player has to quickly say Y or N if the item is food  
    # The faster and more accurate, the better your grade/score  
    # If you answer wrong, you slip and lose a point  
    # If your average is bad, you get a hat with a curse (-2 charisma)  
    # If you do medium, you get slippers (removes intimidation effect)  
    # If you do good, you get the ice ring (lets you cast spells)  
    # Use a 1D10 for some checks  

  
"""-------------------------------------------------------------------------------------------------------------------------------"""  
# If the boss is dead, open the item shop  
    # Show shopkeeper dialogue  
    # (if all 8 rings collected) :
#       "Strong sword (special): Deals 4d8 using STR, normal hit chance, +2 to hit Cronos ONLY – Reward for collecting all 8 rings"  
    # Ask what you want to buy  
    # Show list of items for sale:  
        # Bootle of XP (updates player stats +2) - 1 Gold  
        # Great sword (3d8, high strength, higher chance of missing) - 1 Gold  
        # Rapier (Dexterity weapon, 1d8) - 1 Gold  
        # Wand (can cast “start shooter”, blinds and does 1d6 damage) - 1 Gold  
        # Armor (+5 AC) - 2 Gold  
  
"""-------------------------------------------------------------------------------------------------------------------------------"""  
  
# List of Items / Variables:  
# ice ring (cast spells, -3 DEX to enemy)  
# slippers (removes intimidation effect)  
# hat with curse of binding (removes -2 charisma)  
# gold (currency to buy stuff)  
# ability: Gorilla warfare (strike twice because enemy is surprised)  
# Rapier of sacrifice (hurts both you and the enemy, 2d20)  
# Graviole wand (permanent +2 DEX, force attack)  
# Meat (heals player)  
# intimidated spell (gives disadvantage)  
# Cyber chip (grants +2 DEX permanently)  
# Cronos’s ability (turn back one turn in time)  
# Bootle of XP (updates player stats +2)  
# Great sword (3d8, strength, higher miss chance)  
# Rapier (Dexterity weapon, 1d8)  
# Wand (can cast “start shooter”, blinds enemy and 1d6 damage)  
# Armor (+5 AC)  
# sword  
# cronos teleport (teleport into Cronos's realm)  
#healing potions

    # Strong Sword (Reward for collecting all 8 rings)  Deals 4d8 damage (uses STR, normal hit chance)  When equipped, gives +2 to hit Cronos  
  
"""-------------------------------------------------------------------------------------------------------------------------------"""  
# How it runs:  
# While the universe/game is running:  
    # While there are still worlds you haven't visited:  
        # Ask the player: "Do you want to go through portal 1 (random) or portal 2 (Cronos's realm)?"  
        # If portal 1:  
            # Pick a random world you haven't been to yet  
            # Go to that world and play through it  
        # If portal 2:  
            # Go to Cronos's world for the final boss fight  
    # If all 8 worlds are discovered/visited:  
        # Go to final boss fight with Cronos  
    # After the game (if player or Cronos is dead):  
        # Ask if player wants to restart  
        # If no, end the game  
        # If yes, reset everything and play again  
  
"""-------------------------------------------------------------------------------------------------------------------------------"""  
