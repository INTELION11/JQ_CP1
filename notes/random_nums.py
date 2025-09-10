# JQ 1st Random Numbers Notes

import random

name = input("what is your name? ").trip()

stat_one = random.randint(1,10) + random.randint(1,10)
stat_two = random.randint(1,10) + random.randint(1,10)
stat_three = random.randint(1,10) + random.randint(1,10)
stat_four = random.randint(1,10) + random.randint(1,10)
stat_five = random.randint(1,10) + random.randint(1,10)
stat_six = random.randint(1,10) + random.randint(1,10)
stat_seven = random.randint(1,10) + random.randint(1,10)

#telling user stat choices
print(f"your stat options are:  {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six} {stat_seven},")


# set stats
strenghth = int(input("wich stat do you want as your streinghth: \n")) +2


print(random.random())
print(random.randint(1,20))
print(f"random number from one to twenty: {random.randint(1,20)}")