# JQ 1st Functions
#set variables first
player_health = 100
monster_health = 100
#define all of our functions
def damage(amount,turn):
    if turn == "player":
        return monster_health - amount, player_health
    else:
        return monster_health, player_health - amount
monster_health, player_health = damage(10, "player")
print(f"monster health; {monster_health}")
print(f"player health; {player_health}")




def add(x,y):
    return y+x

def initials(name):
    #\/ name becomes a list as names
    names = name.split(" ")
    initials = ""
    for name in names:
       initials += name[0]

    return initials

total = add(5,5)
print(total)
print(f"10 + 72 = {add(10,72)}")
x = 0
while x < add(3,9):
    print("duck")
    x+= 1

print("goose")

print(initials("Tia LaRose"))
print(initials("Franco Barboza"))

print(f"a is equal to {ord("a")}")
print(f"97 is equal to {chr(97)}")