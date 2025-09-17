# JQ 1st crew Shares
print("The crew earned a whole bunch of money on the last outing, but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the     shares. The captain of the crew gets 7 shares The first mate gets 3 shares Each member of the crew then gets 1 share but the crew members have all already received $500\n")
while True:
    crewnum = int(input(" How many crew memmbers are there (not including the captain and first mate)?\n"))
    crewgain = float(input(" How much treasure did the pirates gain after this expedition?\n"))


    # maths
    divider = crewnum + 10
    shares = crewgain / divider
    captain = shares * 7
    first_mate = shares * 3
    pre_crew = shares
    crew = pre_crew - 500

    #prints
    print (f"{crewgain} has earned")
    print (f"there are {crewnum} crew members not including the capatin and firstmate")
    print (f"the captain gets {captain:.2f}")
    print (f"the first mate gets {first_mate:.2f}")
    print (f"the crew is still owed {crew:.2f}")