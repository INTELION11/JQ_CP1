# JQ 1st Final Project pseudocode
#Important variables: #STR(if they hit or miss an attack, added to their roll) #DEX(if they dodge an attack with the roll item and adds to AC)  #HP, action, inventory, monster stats, been_to_worlds, worlds_not_been_to,
# import random
#import time
# create inventory as a list, all items that can be used in hand are stored here for atack and healing
# (f"\033[38;2;160;160;160mWelcome adventurer, your name is lyte\033[1m") - make the text color light grey
# randomize     #STR #DEX 1-20 and #HP 60-70
# stat_opinion = show input "here are your stats: STR DEX HP, tyou have one more chance to re roll, say yes if you want to reroll, say no if you dont"
# if stat_opinion == yes
# randomize     #STR #DEX 1-20 and #HP 60-70
    # show "here are your stats STR DEX HP""
# elif stat_opinion == no
    #show ""
# else
    #show""
# show " Cut scene " 
# function of Desert_hammurabi
"""-------------------------------------------------------------------------------------------------------------------------------"""
#    define desert_hamurabii,The iztec Jungla,mlɒɘЯbɘqɿɒWɘ⑁TTheWarpedrealm,Pangeon,Modern world,Cybercity 3012,Medieval Europe -(choose to fight or wait 2:30 minutes to be teleported anywhere else -modern world)  (STR #DEX , HP #inventory)
    #   show cutscene (descriptive dialouge of the place)
    #   mon_hp = 34(example)
    #    mon_dex = 13(example)
    #   mon_weapon = body (example)
    #combat(Inventory,mon_hp,mon_dex,mon_weapon,STR #DEX, HP #inventory)- player and montser fight to death, (they can choose to use anything in their inventory)(add Weapons and armor modifiers) 
    # (exaustion score for- desert), basic combat function created in a nother project with sligt diferenciations (multiple monsters and -4 dexterity- Cybercity 3012), 
    # (every 2 turns, oxygen poisoning 1d4 - Pangeon)(+4 dex-TheWarpedrealm)(Intimadated(Disadvantage) and -4 STR- Modern world).to use on diferent maps
    #if monster = is dead
    #   add to inventory (meat,gold,time_cristal, ancient artifact(depends on the map))
    #   show ( inventory updates: {inventory}
    # open shop keeper, dialouge and show items to buy from him, exit function, made using the grocery list from another project
    #if the player is dead loop universe to the start
"""-------------------------------------------------------------------------------------------------------------------------------"""
# define Final Boss
    # cronos dialouge dialouge 
    #combat(mon_hp,mon_dex,mon_weapon,STR #DEX, HP #inventory)- player and montser fight to death, the final boss cronos can attack 6 times as a hexaweilder, for every map that you have been to he looses one of his 6 arms, he also looses a turn
    #if you defeat him you win, give option to restart
    # if you loose sad dialouge, give option to restart
"""-------------------------------------------------------------------------------------------------------------------------------"""
# define Ötzi’s Tusdra
    # dialouge
    # minigame of cooking:
    # a stop watch will start and you will have to quickly say N or Y if an item is food, based on howmany items you got on how many seconds it will get an avarage and grade you on that, if you answer incorrectly you slip and loose a point
    # bad avarage you gain a hat with curse of binding that removes -2 charisma
    # if medium you gain slippers removes the intimidation effect from you
    # if good you gain (ice ring to cast spells)
    #1D10
"""-------------------------------------------------------------------------------------------------------------------------------"""
# if the boss is dead use function Item shop
    #dialouge
    # what would you like to buy? 
    # #show list of shoppable items ((Bootle of XP updates player stats +2)- 1 Gold (Great sword (3d8) strength, higher chance of missing)- 1 Gold  
    # (Rapier Dexterity weapon)(1d8)- 1 Gold  (Wand ability to cast “start shooter” blinds enemy and deals 1d6 damage)- 1 Gold  (Armor +5 AC)- 2 Gold  )
"""-------------------------------------------------------------------------------------------------------------------------------"""


# Items/ variables
# ice ring to cast spells, -3 dex to enemy
# slippers removes the intimidation effect from you
# a hat with curse of binding that removes -2 charisma
# gold
# ability : Gorilla warfare: strike twice becouse enemy is surprised
# The Rapier of sacrifice ( Stab yourself stabs your enemy, stabbing your enemy stabs yourself,) (2d20)
# Graviole wand ( permanent +2 dexterity bonus) (force attack)
# Meat
# intimidated spell
# Cyber chip ( grants +2 Dexterity permanently)
# cronos ‘s ability is to turn back one turn in time
# Bootle of XP (updates player stats +2)
# Great sword (3d8)( strength, higher chance of missing)
# Rapier (Dexterity weapon)(1d8)
# Wand ability to cast “start shooter”( blinds enemy and deals 1d6 damage)
# Armor +5 AC 
# sword
# cronos teleport (teleport into cronos's realm)

"""-------------------------------------------------------------------------------------------------------------------------------"""
#How it runs:
#while universe is True
    #While there are still discoverable worlds
        #   cristal_option is "do you want to go though portal 1 (random) or 2 (cronos's realm)"
        #if you go through potal 1
        #  option one is random between 1-8,  the number decides what world they teleport into (apart from the world they have been to, if there are none left then break)
        # if you go thpough portal 2 go to final boss cronos's world
    # use function Final Boss if worlds 1-8 are discovered already
    # ask user is the want to restart the game if player = dead or cronos = dead 
    #if no then break
    #if yes continue


"""-------------------------------------------------------------------------------------------------------------------------------"""
