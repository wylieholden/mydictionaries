# 1) print out the value for the key 'history' using the dictionary below


sampleDict = {
    "class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}
}

score = sampleDict["class"]["student"]["marks"]["history"]
print(score)

# 2) Add 2 inches to the son's height. note add, not hardcode

dict = {
    "son's name": "Lucas",
    "son's eyes": "green",
    "son's height": 32,
    "son's weight": 25,
}

dict["son's height"] += 2

# 3) Given a Python dictionary, Change Brad’s salary to 8500. note this should be hardcoded

sampleDict = {
    "emp1": {"name": "Jhon", "salary": 7500},
    "emp2": {"name": "Emma", "salary": 8000},
    "emp3": {"name": "Brad", "salary": 6500},
}

sampleDict["emp3"]["salary"] = 8500


# 4 )Given the dictionary below, add a new key - 'work' with the values shown below:
#       "work": ["Apology", "Phaedo", "Republic", "Symposium"]

dict = {
    "name": "Plato",
    "country": "Ancient Greece",
    "born": -427,
    "teacher": "Socrates",
    "student": "Aristotle",
}

dict["work"] = ["Apology", "Phaedo", "Republic", "Symposium"]
print(dict)
