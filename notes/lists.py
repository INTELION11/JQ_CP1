# JQ 1st List Notes
import random
# in brakets, separated by commas, proper data types
sibs = ["alex", "katie", "andrew", "vienna", "tia", "treyson", "jeferson", "jake"]

print(sibs[5])
print(random.choice(sibs, weights=(10,10,10,10,10,10,10,10,20,10), k=5))
print(f" the lists is {len(sibs)} people long")
print(sibs)
sibs[0] = "eric"
sibs[6:-1] = ["xavier", "hailey"]
sibs.pop()
sibs.pop(3)
sibs.remove("andrew")
#sibs.clear()
#sibs.append("andrew")
sibs.insert(2, "andrew")
sibs.extend(["joseph", "izrael", "zee"])
print(sibs)

#board = [[1,2,3],
#        [4,5,6]
 #       [7,8,9]
#       ]

fruit = ("apple", "orange", "pineapple") # tuple ordered, not changable

veggies = {"spinash", "kale", "brocoli", "carrot"} #set is unordered and changeable
print(veggies)
