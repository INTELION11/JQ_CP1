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
 
  

def shop(player_gold, inventory, player_str, player_dex, player_ac):  
    shop_items = [  
        {"name": "Bootle of XP (+2 to all stats)", "price": 4, "effect": "xp"},  
        {"name": "Great sword (3d8, high strength, higher miss chance)", "price": 3, "effect": "greatsword"},  
        {"name": "Rapier (Dexterity weapon, 1d8)", "price": 2, "effect": "rapier"},  
        {"name": "Wand (can cast 'star shooter', blinds & 1d6 dmg)", "price": 2, "effect": "wand"},  
        {"name": "Armor (+5 AC)", "price": 4, "effect": "armor"},  
        {"name": "Healing potion (heals 20)", "price": 2, "effect": "heal20"},  
        {"name": "Meat (heals 10)", "price": 1, "effect": "heal10"}  
    ]  
    sprint("\nWelcome to the shop! Your gold: " + str(player_gold))  
    while True:  
        sprint("\nItems for sale:")  
        for i, item in enumerate(shop_items, 1):  
            sprint(f"{i}. {item['name']} - {item['price']} gold")  
        sprint(f"{len(shop_items)+1}. Exit shop")  
        choice = input("Enter the number of the item you want to buy: ").strip()  
        if not choice.isdigit():  
            sprint("Please enter a number.")  
            continue  
        choice = int(choice)  
        if choice == len(shop_items) + 1:  
            break  
        elif 1 <= choice <= len(shop_items):  
            selected = shop_items[choice-1]  
            if player_gold < selected["price"]:  
                sprint("Not enough gold!")  
                continue  
            player_gold -= selected["price"]  
            if selected["effect"] == "xp":  
                player_str += 2
                player_dex += 2
                player_ac += 2
                sprint("You feel all your abilities increase!")  
            elif selected["effect"] == "greatsword":  
                inventory["greatsword"] = 24  
                sprint("Great sword added to inventory!")  
            elif selected["effect"] == "rapier":  
                inventory["rapier"] = 8  
                sprint("Rapier added to inventory!")  
            elif selected["effect"] == "wand":  
                inventory["wand"] = 6  
                sprint("Wand added to inventory!")  
            elif selected["effect"] == "armor":  
                player_ac += 5  
                sprint("Armor equipped! +5 AC")  
            elif selected["effect"] == "heal20":  
                inventory["healing_potion"] = "heal20"  
                sprint("Healing potion added to inventory!")  
            elif selected["effect"] == "heal10":  
                inventory["meat"] = "heal10"  
                sprint("Meat added to inventory!")  
        else:  
            sprint("Invalid choice.")  
    return player_gold, inventory, player_str, player_dex, player_ac  
 

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

def cronos_combat(player_hp, player_str, player_ac, player_dex, cronos_hp, cronos_ac, cronos_dmg, inventory, player_exhaustion, cristals_collected):  
    turn = 1  # Player goes first  
    max_attacks = 6  
    sprint("\nThe final battle begins! Cronos looms before you...")  
    while player_hp > 0 and cronos_hp > 0:  
        if turn == 1:  
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
                to_hit = r.randint(1, 20) + player_str // 4 - player_exhaustion  
                sprint(f"You rolled a {to_hit} to hit!")  
                if to_hit >= cronos_ac:  
                    dmg = max(1, r.randint(1, inventory[item]) + player_str // 4 - player_exhaustion)  
                    cronos_hp -= dmg  
                    sprint(f"You hit Cronos for {dmg} damage! Cronos has {cronos_hp} HP left.")  
                else:  
                    sprint("You missed!")  
            else:  
                sprint(f"You can't do that with {item}.")  
                continue  
            turn = 2  
        else:  
            # Cronos's turn  
            attacks = max(1, max_attacks - cristals_collected)  
            sprint(f"Cronos attacks {attacks} times!")  
            hit_count = 0  
            for i in range(attacks):  
                to_hit = r.randint(1, 20)  
                if to_hit >= player_ac + player_dex // 4:  
                    dmg = r.randint(1, cronos_dmg)  
                    player_hp -= dmg  
                    hit_count += 1  
                    sprint(f"Cronos's attack {i+1}: Hits you for {dmg} damage! You now have {player_hp} HP.")  
                    if player_hp == 0:  
                        break  
                else:  
                    sprint(f"Cronos's attack {i+1}: Missed!")  
            turn = 1  
  
    if player_hp < 0:  
        sprint("You have fallen to Cronos. The world fades away...")  
        return 'lose', player_hp, player_str, player_dex, player_ac, player_exhaustion  
    elif cronos_hp < 0:  
        sprint("You have defeated Cronos! The world is saved!")  
        return 'win', player_hp, player_str, player_dex, player_ac, player_exhaustion   
    return 'error', player_hp, player_str, player_dex, player_ac, player_exhaustion 

  
def desert_hammurabi(player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion,maximum_player_health):  
    sprint("\033[38;5;223mYou step into a scorching, endless desert where ancient ruins rise from the shifting sands. The sun beats down as mirages shimmer on the horizon. Suddenly, a massive stone golem, carved with old cuneiform script, lumbers out from behind a crumbling ziggurat, its eyes glowing with ancient fury.\033[0m")  
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
    player_hp = maximum_player_health; 
     
    player_gold, inventory, player_str, player_dex, player_ac = shop(player_gold, inventory, player_str, player_dex, player_ac) 
    return player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion, maximum_player_health  

def iztec_Jungla(player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion,maximum_player_health):  
    sprint("\033[38;5;223mA Thick vines and towering trees create a tangled canopy above you in a humid, vibrant jungle. The air buzzes with insects and the calls of distant birds. From the undergrowth leaps a jaguar guardian, its fur marked with mystical patterns and its teeth bared for battle.\033[0m")  
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
            maximum_player_health += r.randint(1,5)
            sprint(f"Your HP stat increased, it is now {maximum_player_health}")
    inventory["dagger"] = 10
    player_hp = maximum_player_health;  
    player_gold, inventory, player_str, player_dex, player_ac = shop(player_gold, inventory, player_str, player_dex, player_ac) 
    return player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion, maximum_player_health  
def TheWarpedrealm(player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion,maximum_player_health):  
    sprint("\033[38;5;223mReality twists and bends around you; colors shift and shapes melt into impossible forms. Gravity feels odd here, and echoes bounce in strange directions. Out of a swirling portal crawls a many-eyed abomination, its limbs constantly changing and its stare unblinking.\033[0m")  
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
    player_hp = maximum_player_health;  
    player_gold, inventory, player_str, player_dex, player_ac = shop(player_gold, inventory, player_str, player_dex, player_ac) 
    return player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion, maximum_player_health  
def Pangeon(player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion,maximum_player_health):  
    sprint("\033[38;5;223mYou find yourself on a primeval plain, where ferns grow taller than houses and the air is thick with the scent of earth and rain. The ground shakes as a gigantic saber-toothed cat stalks out from the tall grass, muscles rippling and fangs glinting.\033[0m")  
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
    player_hp = maximum_player_health;  
    player_gold, inventory, player_str, player_dex, player_ac = shop(player_gold, inventory, player_str, player_dex, player_ac) 
    return player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion, maximum_player_health  
def Modern_world(player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion,maximum_player_health):  
    sprint("\033[38;5;223mNeon lights flicker and cars zoom by on sleek asphalt streets. Towering skyscrapers loom overhead, and digital billboards flash everywhere. Blocking your path, a street-tough cyborg mercenary steps forward, metal fists clenched, ready to pick a fight.\033[0m")  
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
    player_hp = maximum_player_health;  
    player_gold, inventory, player_str, player_dex, player_ac = shop(player_gold, inventory, player_str, player_dex, player_ac) 
    return player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion, maximum_player_health  
def Cybercity_3012(player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion,maximum_player_health):  
    sprint("\033[38;5;223mYou are surrounded by gleaming towers and flying vehicles in a city of the far future. Holograms and robots bustle everywhere. Suddenly, a rogue android with shifting armor and blazing plasma blades drops down from above, targeting you as its next opponent.\033[0m")  
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
    player_hp = maximum_player_health;  
    player_gold, inventory, player_str, player_dex, player_ac = shop(player_gold, inventory, player_str, player_dex, player_ac) 
    return player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion, maximum_player_health  
def Medieval_Europe(player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion,maximum_player_health):  
    sprint("\033[38;5;223mStone castles rise above rolling green hills and cobblestone villages. The air is filled with the clatter of armor and the smell of roasting meat. From a nearby tourney ground, a black-armored knight mounted on a warhorse charges toward you, lance lowered for the attack.\033[0m")  
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
    player_hp = maximum_player_health;  
    player_gold, inventory, player_str, player_dex, player_ac = shop(player_gold, inventory, player_str, player_dex, player_ac) 
    return player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion, maximum_player_health  

def otsiz_tundra_minigame():  
    import time  
  
    # Items: some are food, some are not  
    items = [  
        ("dried meat", True),  
        ("stone axe", False),  
        ("berries", True),  
        ("animal skin", False),  
        ("fish", True),  
        ("wooden bowl", False),  
        ("acorns", True),  
        ("bone needle", False),  
        ("wild onions", True),  
        ("flint knife", False)  
    ]  
  
    sprint("\nWelcome to the Ötzi's Tusdra Minigame!")  
    sprint("Quickly type 'y' if the item is food or 'n' if it is not food.")  
  
    correct = 0  
    wrong = 0  
  
    random_items = r.sample(items, len(items))  # shuffled order  
  
    start_time = time.time()  
  
    for item, is_food in random_items:  
        sprint(f"\nIs '{item}' food? (y/n)")  
        answer = input().strip().lower()  
        if (answer == "y" and is_food) or (answer == "n" and not is_food):  
            sprint("Correct!")  
            correct += 1  
        else:  
            sprint("Wrong! You slip and lose a point.")  
            wrong += 1  
  
    end_time = time.time()  
    total_time = end_time - start_time  
    score = (correct - wrong) / max(total_time, 1)  # avoid division by zero  
  
    sprint(f"\nYou got {correct} right and {wrong} wrong in {total_time:.1f} seconds.")  
    sprint(f"Your performance score: {score:.2f}")  
  
    # Prize logic:  
    if score == 0.1:  
        sprint("You get a hat with a curse! (-2 charisma)")  
        prize = "hat_with_curse"  
    elif score == 0.25:  
        sprint("You get some old slippers! (removes intimidation effect)")  
        prize = "slippers"  
    else:  
        sprint("You get the legendary ice ring! (lets you cast spells)")  
        prize = "ice_ring"  
  
    # Example: Add prize to inventory  
    # inventory[prize] = True  
  
    # Optional: Use a 1d10 for bonus checks  
    d10 = r.randint(1, 10)  
    sprint(f"You roll a D10 and get a {d10} (for use in later events).")  
  
    return prize, score, d10  

def main_game_loop():  
    # --- Initialize inventory and player stats ---  
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
    cristal=0
    player_gold = 0  
    player_exhaustion = 0  
    player_meat = 0  
    maximum_player_health = player_hp  
  
    all_maps = [  
        "desert_hammurabi",  
        "iztec_jungla",  
        "warpedrealm",  
        "pangeon",  
        "modern_world",  
        "cybercity_3012",  
        "medieval_europe",  
        "otsiz_tundra"  
    ]  
    visited_maps = []  
  
    while True:  
        while len(visited_maps) < len(all_maps) - 1:  # leave final boss  
            sprint("\nDo you want to:\n1. Go to Cronos's realm (final boss)\n2. Enter a random portal (new world)?")  
            choice = input("Enter 1 for Cronos, 2 for a new map: ").strip()  
            if choice == "1":  
                break  
            else:  
                unvisited = [m for m in all_maps if m not in visited_maps and m != "otsiz_tundra"]  
                if not unvisited:  
                    sprint("No more unexplored worlds!")  
                    break  
                chosen_map = r.choice(unvisited)  
                visited_maps.append(chosen_map)  
                sprint(f"\nYou travel to {chosen_map.replace('_', ' ').title()}...")  

                if chosen_map == "desert_hammurabi":  
                    player_hp, player_dex, player_str, player_ac,inventory, player_gold, player_exhaustion, player_meat = desert_hammurabi(  
                        player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion, player_meat)
                    cristal += 1  
                elif chosen_map == "iztec_jungla":  
                    player_hp, player_dex, player_str, player_ac,inventory, player_gold, player_exhaustion, player_meat = iztec_Jungla(  
                        player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion, player_meat)  
                    cristal += 1
                elif chosen_map == "warpedrealm":  
                    player_hp, player_dex, player_str, player_ac,inventory, player_gold, player_exhaustion, player_meat = TheWarpedrealm(  
                        player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion, player_meat)
                    cristal += 1  
                elif chosen_map == "pangeon":  
                    player_hp, player_dex, player_str, player_ac,inventory, player_gold, player_exhaustion, player_meat = Pangeon(  
                        player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion, player_meat)  
                    cristal += 1
                elif chosen_map == "modern_world":  
                    player_hp, player_dex, player_str, player_ac,inventory, player_gold, player_exhaustion, player_meat = Modern_world(  
                        player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion, player_meat) 
                    cristal += 1 
                elif chosen_map == "cybercity_3012":  
                    player_hp, player_dex, player_str, player_ac,inventory, player_gold, player_exhaustion, player_meat = Cybercity_3012(  
                        player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion, player_meat)  
                    cristal += 1
                elif chosen_map == "medieval_europe":  
                    player_hp, player_dex, player_str, player_ac,inventory, player_gold, player_exhaustion, player_meat = Medieval_Europe(  
                        player_hp, player_dex, player_str, player_ac, inventory, player_gold, player_exhaustion, player_meat)  
                    cristal += 1
                elif chosen_map == "otsiz_tundra":  
                    prize,score,d10 = otsiz_tundra_minigame()  
                    inventory[prize] = True 
                    cristal += 1 
  
                player_gold, inventory, player_str, player_dex, player_ac = shop(  
                    player_gold, inventory, player_str, player_dex, player_ac)  
  
                if player_hp < 0:  
                    sprint("\nYou have died! Would you like to restart? (y/n)")  
                    if input().strip().lower() == "y":  
                        return main_game_loop()  
                    else:  
                        sprint("Thanks for playing!")  
                        sys.exit()  
  
        sprint("\nYou face Cronos, the final boss!")  
        cristals_collected =cristal
        if cristals_collected >= 6:
            cristals_collected = 6

        cronos_hp = 100  
        cronos_ac = 15  
        cronos_dmg = 16  
        cristals_collected = len(visited_maps)  
        result, player_hp, player_str, player_dex, player_ac, player_exhaustion = cronos_combat(  
            player_hp, player_str, player_ac, player_dex, cronos_hp, cronos_ac, cronos_dmg, inventory, player_exhaustion, cristals_collected  
        )  
        if result == 'win':  
            sprint("\nCongratulations! You have defeated Cronos and won the game!")  
        elif result == "lose":
            sprint("\nYou were defeated by Cronos.") 
        elif result == "error":
            sprint(" there was an error therefore you win by default")
  
        sprint("\nWould you like to restart the adventure? (y/n)")  
        if input().strip().lower() == "y":  
            return main_game_loop()  
        else:  
            sprint("Thanks for playing!")  
            sys.exit()  
  
 
main_game_loop()  

 

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
