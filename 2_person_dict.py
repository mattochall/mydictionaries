person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}


print(person)

# print out the name of the second child

print(person["children"][1])

# print out the name of the cat

print(person["pets"]["cat"])


# iterate through all children and print out each child

for item in person["children"]:
    print(item)


# print out the pets in this format:
# Type of pet: dog Name of Pet: Fido

for item in person["pets"]:
    print("type of pet:", item, "name of pet: ", person["pets"][item])
