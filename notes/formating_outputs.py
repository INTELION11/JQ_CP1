# JQ 1st Formating Outputs Notes

#how do i write the formating method
name = "eric"
age = 1200
money = 25000.1
percent = .74
print("hello {}, you are {:b}. that is so old! you have ${:.2f} you must be rich, random percent is {:%}".format(name, age, money, percent))
#print("hello {}, you are {:E}. that is so old!".format(name, age))
#print("hello {}, you are {:,}. that is so old!".format(name, age))


print(f"Hello {name}, you are {age:,}. that is soo old! you have ${money:.2f} you must be rich! random perecent is {88/100:%}") # <--can type code directly into brakets
