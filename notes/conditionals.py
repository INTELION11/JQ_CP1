# JQ 1st Conditional Notes
import random
player_hp = 20
player_attack = 2
player_defense = 5
player_damage = 5

monster_hp = 15
moster_attack = 3
monster_damage = 10
monster_defense = 2

hit_roll = random.randint(1,20)
damage_roll = random.randint(1,8) + player_damage
if hit_roll == 20:
    print("You got a crit!, roll for damage twice!")
    damage_roll = random.randint(1,8) + random.randint(1,8) + player_damage
    print(f"you did {damage_roll - monster_defense} points of damage.")
    monster_hp -= (damage_roll-monster_defense)
elif hit_roll == 1:
    print("You Rolled a Critical failure and sliped under the monster and he fell on top of you! now the monster gets to attack you")
    damage_roll =  random.randint(1,12) + monster_damage
    player_hp -= (damage_roll-player_defense)
    print(f"the Monster dealt {damage_roll}, your hp is now {player_hp}")
elif hit_roll + player_attack >= 12:
    print("you hit! roll for damage")
    damage_roll = random.randint(1,8) + player_damage
    if damage_roll > monster_defense:
        print(f"you did {damage_roll - monster_defense} points of damage.")
        monster_hp -= (damage_roll-monster_defense)
    else:
        print("you did no damage")
else:
    print("you missed")
print("your turn is over")

if True:
    attack_roll = random.randint(1,20) + moster_attack
    print(f"the monster dealt {attack_roll}")
#comparison operators
# greater than >
#less than <
# equalt to ==
# not equal !=
# greater than or equal to >=
#less than or equal to <=   