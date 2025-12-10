# JQ 1st Final Project pseudocode  
import random as r
import time as t
import sys
def sprint(text, delay=0.025):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        t.sleep(delay)
    print()
# Important variables:  
# STR (used to see if you hit or miss an attack, adds to your attack roll)  
# DEX (used to see if you dodge an attack, adds to your Armor Class)  
# HP (your health points)  
# action (what the player chooses to do)  
# inventory (a list of all the items you find and use for attacking or healing)  
# monster stats (each monster will have its own HP, DEX, and weapon)  
# been_to_worlds (list of worlds you have already visited)  
# worlds_not_been_to (list of worlds you still need to visit)  
# import random (to make things random)  
# import time (to control time for things like minigames)  

# create inventory as a list, all items you can use in hand for attack and healing get stored here  
inventory = {
    "greatsword" : 12
}
sprint("\033[37mShow a welcome message to the player, make the text color light grey  Let the player know their name is Lyte.\033[0m")
# Show a welcome message to the player, make the text color light grey  
# Let the player know their name is Lyte  
  
# Randomly pick the player's STR (1-20)  
# Randomly pick the player's DEX (1-20)  
# Randomly pick the player's HP (60-70)  
str = r.randint(1,20)
dex = r.randint(1,20)
hp = r.randint(60,70)
ac = r.randint(9,11)
# Show the player their stats 
sprint(f" Your stats: \n {str}\n {dex}\n {hp}\n {ac}")
action = input("You have one more chance to reroll, say yes if you want to reroll, say no if you don't\n")
# Ask if they want to reroll their stats: "You have one more chance to reroll, say yes if you want to reroll, say no if you don't"  
if action == "yes":  
    str = r.randint(1,20)
    dex = r.randint(1,20)
    hp = r.randint(60,70)
    ac = r.randint(9,11)
    # Show the player their stats 
    sprint(f" Your stats: \n {str}\n {dex}\n {hp}\n {ac}")
elif action == "no": 
    print() 
    # Continue with these stats  
else:  
    # Continue anyway 
    print() 
  

# Show a cutscene to start the story 
sprint(" meets cronos, cronos throws him away")
"""-------------------------------------------------------------------------------------------------------------------------------"""  

# Define all the worlds: Desert_hammurabi, Iztec_Jungla, Warpedrealm, Pangeon, Modern_world, Cybercity_3012, Medieval_Europe, Otzis_Tusdra  
def desert_hammurabi(health,dexterity,stren,defense,invent):

   
    sprint("\033[38;5;223mcutscene describing the desert and monster appears.\033[0m")
    monster_health = 30  
    monster_defense = 13  
    monster_damage = 12  
    
    
    def monster_turn(player_health, player_defense):  
        strike = r.randint(1, 20)  
        if strike >= player_defense:  
            sprint("\033[38;5;223mthe monster hits you!\033[0m")  
            return r.randint(1, 12)  
        else:  
            sprint("\033[38;5;223mthe sand snake missed!\033[0m")  
            return 0  
    
    def player_turn(health,stren,defense,invent,monster_hp,monster_def,monster_dmg):  
        sprint(f"your stats: \n {health} HP\n AC: {defense}\n {inventory}")  
        action = input("\033[38;5;223mits your turn, what is your action, heal or attack\n\033[0m").strip().lower()  
        while True:
            result = {"health": health,"monster_health": monster_health, }  
            if action == "heal":  
                heal_amt = r.randint(1, 10)  
                result["health"] += heal_amt  
                sprint(f"you healed {heal_amt} points! your health is now {result['health']} hp")   
            elif action == "attack":  
                inpat = input("\033[38;5;223m what weapon or item in inventory will you use?\n\033[0m").strip().lower()
                if inpat not in invent:
                    continue
                your_attack = r.randint(1, 20)  
                sprint(f"you rolled a {your_attack} to hit!")  
                if your_attack >= monster_def:  
                    dmg = r.randint(1, invent[inpat]) + round(stren/4)
                    result["monster_health"] -= dmg  
                    sprint(f"you hit the monster for {dmg} points! monster has {result['monster_health']} hp left")  
                else:  
                    sprint("you missed!")  
            else:  
                sprint("not a valid action, try again!")  
                continue
            return player_turn(result["health"],result["monster_health"], monster_defense,)
        return result  
    
    sprint("Welcome to fighting! First I need to know some things about you!")    
    turn = r.randint(1, 2)  
    
    while monster_health > 0 and health > 0:  
        if turn == 1:  
            result = player_turn(health,dexterity,stren,defense,invent,monster_health,monster_defense,monster_damage)  
            health = result["health"]  
            monster_health = result["monster_health"]  
            turn = 2  
        elif turn == 2:  
            sprint("its the monsters turn!")  
            t.sleep(1)  
            temp_defense = defense  
            health -= monster_turn(health, temp_defense)  
            sprint(f"you have {health} hp remaining")  
            turn = 1  
    
    if health <= 0:  
        sprint("you have fallen in battle. try again next time!")  
    elif monster_health <= 0:  
        sprint("you win! monster is defeated, that was too easy right?!")  
desert_hammurabi(hp,dex,str,ac,inventory)
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
