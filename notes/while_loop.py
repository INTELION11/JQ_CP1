# JQ 1st For Loops Notes
#these do the same thing
#num=1 # iterator
#while num <= 20:#<--- end break condition
#    print(num)
#    num += 1 # increase iterator
#
#
# these do the same thing
 #  iterator
#    |
#   \/
#for num in range(1,21):# <--- Break/ end condition
#    print(num) # what loop does
import time
import random
num = 1

while num <= 20:
    time.sleep(.001)
    print(num)
    num += 1 # prevents infinite loop

goose = random.randint(1,20)
count = 1
while count != goose:
    count += 1
    print("duck")
    if count == 6:
        break
    
else:
    print("GOOSE!!!")

print("the code is done")






i = 0

while i < 20:
    i+= 1
    if i ==10:
        print("i is 10")
        continue
    else:
        print(f"{i} Iteration of the loop")
    

print("the loop is ended")
