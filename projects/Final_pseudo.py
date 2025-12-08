# JQ 1st Final Project pseudocode  
import random as r
import time as t
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
inventory = {}
print("# Show a welcome message to the player, make the text color light grey  Let the player know their name is Lyte ")
# Show a welcome message to the player, make the text color light grey  
# Let the player know their name is Lyte  
  
# Randomly pick the player's STR (1-20)  
# Randomly pick the player's DEX (1-20)  
# Randomly pick the player's HP (60-70)  
str = r.randint(1,20)
dex = r.randint(1,20)
# Show the player their stats  
# Ask if they want to reroll their stats: "You have one more chance to reroll, say yes if you want to reroll, say no if you don't"  
# If the player says yes:  
    # Randomize STR, DEX, HP again  
    # Show the new stats  
# Else if the player says no:  
    # Continue with these stats  
# Else:  
    # Continue anyway  
  
# Show a cutscene to start the story  
  
"""-------------------------------------------------------------------------------------------------------------------------------"""  
# Define all the worlds: Desert_hammurabi, Iztec_Jungla, Warpedrealm, Pangeon, Modern_world, Cybercity_3012, Medieval_Europe, Otzis_Tusdra  
  
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
