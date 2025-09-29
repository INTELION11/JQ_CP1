# JQ 1st DEBUGGING NOTES!


#Syntax Error - grammar error
#print"Vienna"
# => read error message, go to that line of code, fix the syntax

#Logic Errors - we gave the wrong steps
numone = "2"
numtwo = "5"

print (numone + numtwo)

# Have well thought out plan, step by step go thorough our logic

# Run-time Error
#dont like brute force debugging
import random
while True:
    denomanator = random.randint(0,5)
    print(f"denomanator is {denomanator}")
    print(10/denomanator)
    #read the error that pops up in terminal, go to the line
