import random

## They Key will always be on the left (a string value), and the value will always be the right (it can be anything
# a list, image, video, etc). Everything in Python is an object and an object has two distinct features, attributes and
# methods. Json file is a way to exchange information online.
# API is a
#


phonebook = {}  # this is an empty dictionary

phonebook = {
    "Chris": "555−1111",
    "Katie": "555−2222",
    "Joanne": "555−3333",
}  # this dictionary has hard coded values in it

# Key is the name of the individuals, the value is the cooresponding phone numbers


print()
print("*****  start section 1 - print dictionary ********")
print()

mydictionary = dict(m=8, n=9)
print(mydictionary)

print(len(phonebook))  # shows number of elements in the dictionary

print(
    type(phonebook)
)  # tells you you're dealing with a dictionary (shows type of object you're dealing with)


print()
print("*****  end section 1 ********")
print()


print()
print("*****  start section 2 - search dictionary ********")
print()


# get chris's phone number from dictionary. When you want to get a value from a dictionary you
# give it the key and then you get a value. Lowercase and Uppercase Chris aren't the same, Python is
# case senesitive.

# phone = phonebook["Chris"]
# print(phone)

name = "Chris"

if name in phonebook:
    print(phonebook[name])
else:
    print(f"{name} is not in the phonebook")


print()
print("*****  end section 2 ********")
print()


print()
print("*****  start section 3 - edit/append dictionary ********")
print()

print(phonebook)

phonebook["Chris"] = "555-0123"
phonebook["Joe"] = "555-444"

print(phonebook)

# how to edit, update, or append

print()
print("*****  end section 3 ********")
print()


print()
print("*****  start section 4 - delete/remove from dictionary ********")
print()

print(phonebook)

del phonebook["Chris"]

print(phonebook)


print()
print("*****  end section 4 ********")
print()


print()
print("*****  start section 5 - iterate through keys, values, items ********")
print()
# default option is just the keys, not the values

for k in phonebook:
    print(f"The key is {k} and the value is {phonebook[k]}")

for value in phonebook.values():
    print(value)
    # method values belongs to the dictionary class, allows you to iterate through the values only

for key, value in phonebook.items():
    print(f"The key is {key} and the value is {value}")

for ph_tuple in phonebook.items():
    print(ph_tuple)

print()
print("*****  end section 5 ********")
print()

print()

print("*****  start section 6 - using get and clear ********")
print()

phone = phonebook.get("Chris", "999")
print(phone)

phonebook.clear()
print(phonebook)

print()
print("*****  end section 6 ********")
print()


print()
print("*****  start section 7 - using pop method ********")
print()

remove = phonebook.pop("Chris", "Not Found")
print(remove)
print(phonebook)


print()
print("*****  end section 7 ********")
print()


print()
print("*****  start section 8 - using popitem ********")
print()

a = phonebook.popitem()

print(a)
print(phonebook)
# always pops out the last item, there is no random item for dictionaries. There is a work around with lists

print()
print("*****  end section 8 ********")
print()


print()
print("*****  start section 9 - using random and converting to list ********")
print()

phonebook_list = list(phonebook)
print(phonebook_list)

random_key = random.choice(phonebook_list)  # this method only works on lists
print(random_key)
print(phonebook[random_key])

print(
    phonebook[random.choice(list(phonebook))]
)  # same code as above but one single line

print()
print("*****  end section 9 ********")
print()
