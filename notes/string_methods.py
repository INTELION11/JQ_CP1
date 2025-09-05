#JQ 1st String Methods

subject = "computer Programming 1"

print(subject.upper())

print(subject)
print(subject.center(100))

#STUPID/IDIOT Proofing Inputs
color = input("What is your favor color?").strip().lower().capitalize()
# lower makes it lowercase, 
# upper makes it all uper case, 
# strip removes spaces at the beggining and end
#capitalize, capitalizes the first letter ogf the first word
#titile(), it makes the first letter of all the words capitalied
full_name = input("What is your full name?").strip().title()
print("Thats cool, " + full_name + " i like " + color + " too!")
print("Thats cool, {full_name} i like {color} too!".format(full_name=full_name, color=color))

#f-string
#print(f"Thats cool, {full_name} i like {color} too!")
pi = "500"
# print(f" we all know pi, its {pi:.3f}") # it rounds and lets you choose the decimal places

print(pi.isdigit()) # has to be intiger
print(pi.isdecimal())
sentence = "the quick brown fox jumps over the lazy dog."
word = "brown"
print(sentence.find(word))
start = sentence.index("lazy")
length = len("lazy")
print(sentence[start:start+length])
print(sentence.replace(word, "swims"))