# JQ 1st *Args and **Kwargs


def hello(name = "tia", age = 29):
    return f"hello {name} you are {age}"


print(hello())
print(hello("treyson",19))
print(hello("vienna"))
print(hello(age=37))

def hello(*names, **kwargs):
    print(type(names))
    print(kwargs)
    for n in names:
        print(f"hello {n} {kwargs['last_name']}")

hello("alex","katie","andrew","vienna","tia","treyson","xavier","jake", last_name="laRose")


def full_name(**names):
    if "middle" in names.keys():
        return (f"{names["first"]} {names["middle"]} {names["last"]}")
    else:
        return (f"{names["first"]} {names["last"]}")


print(full_name(age = "???",first="koro", last="sensei"))
print(full_name(age = "so old",first="albus", middle="brian",last="dumbledor"))


def summary(**story):
    sum = ""
    if "name" in story.keys():
        sum += f"{story["name"]} is the main character of this story"
    if "place" in story.keys:
        sum += f"the story takes place in {story["place"]}"
    if "conflict" in story.keys:
        sum += f"the problem is {story["conflict"]}."
    return sum
    
print(summary(name = "lucifier ", place = "a galxay far far away "))
print(summary(name = "harry potter ", conflict = "being born "))
