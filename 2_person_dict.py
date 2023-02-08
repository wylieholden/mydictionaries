person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]  # list within a dict
person["pets"] = {"dog": "Fido", "cat": "Sox"}  # dict within a dict

# print(person)

# print out the name of the second child
print(person["children"][1])

print()
# print out the name of the cat
print(person["pets"]["dog"])

print()
# iterate through all children and print out each child
for child in person["children"]:
    print(child)

print()


# print out the pets in this format:
# type of pet: dog name of pet: Fido
for key in person["pets"]:
    print(f"Type of pet: {key} Name of pet: {person['pets'][key]}")
