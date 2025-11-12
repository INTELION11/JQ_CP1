# JQ 1st period Dictionary Notes!

# saving information in key: value pairs
avatar = {
    "earth": {
    "toph": "sounds like tough and thats just what i am"
    },
    "water": {
        "katara": " it just gave me so much hope",
        "sokka": "im a boomerang guy"
    }
}
print(avatar["earth"]["toph"])
person = {
    #key: value,
    "name": "xavier",
    "age": 22,
    "job": "maverick",
    "sibling":["alex","katie","andrew","vienna","tia","treyson","jake"]
}
person_two = {
    "name": "jake",
    "age":21,
    "job": "NEET",
    "sibling":["alex","katie","andrew","vienna","tia","treyson","xavier"]
}
print(f" Name is {person["name"]}")
print(person.keys())
for key in person.keys():
    if key == "sibling":
        for name in person[key]:
            print(f"{person['name']} has a sibling named {name}")
    else:
        print(f"{key} is {person[key]}")
print(person_two.values())
person_two["age"] += 1
person_two["so"] = "carry"
print(person_two.items())
prinbt()