
names = ["Santosh", "Sarita", "Prashna", "Prexya", "Neesh", "Rima"]
lnames = ["Dahal", "Acharya", "Basnet", "Subedi", "Gautam", "K.C."]
for name in names:
    print(name)
print("Done")

has_santosh = "Santosh" in names
has_nisha = "Nisha" in names

print(has_santosh)
print(has_nisha)
print(len(names))

# Adding in list
names.append("John")

new_name = "Gita"
names.append(new_name)
print(names)

new_name = "Kumar"
if new_name in names:
    print(new_name + " already in list.")
else:
    names.append(new_name)
    print(new_name + " added to the list.")
print(names)

# Change List
names[6] = "Dahal"
print(names)
# Combine list
names.extend(lnames)
print(names)
santosh = names.count("Santosh")
dahal = names.count("Dahal")
print("Total Santosh " + str(santosh))
print("Total Dahal " + str(dahal))

for name in names:
    if name == "Dahal":
        names.remove("Dahal")
names.sort(reverse=True)
print(names)

names.clear()
print(names)
available_toppings = ['musroom', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']
request_toppings = ['musroom', 'french fries', 'extra cheese']

for reqest_topping in request_toppings:
    if reqest_topping in available_toppings:
        print(f"Adding {reqest_topping}.")
    else:
        print(f"Sorry, we don't have {reqest_topping}.")
print("Finished making pizza.\n")

# Ckecking that a list is not empty

request_toppings = []
if request_toppings:
    for request_topping in request_toppings:
        print(f"Adding {request_topping}.")
    print("Finished making Pizza.\n")
else:
    print("Are you sure do you want pizza?")
print("Done Checking List\n")

# Slicing list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print(f"not Reverse {players}")
players.reverse()
print(f"Reverse {players}")
players.sort()
print(f"Sort {players}")
print("Finished slicing list\n")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on ny team:")
count = 1
for player in players[:3]:
    print(f"This is {count} players name: {player.title()}")
    count = count + 1
print("Looping complite.\n")

# Copying list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print(f'My favoriate food are: {my_foods}.')
print(f"My friend favoriate food are: {friend_foods}.")
print('Done Copy list.\n')

# Tuples
dementions = (200, 50)
print(dementions[0])
print(dementions[1])
print('Done Tuple Defining.\n')
# looping All value in a tuple
dementions = (200, 50)
for demention in dementions:
    print("Dementions " + str(demention))
print("Done looping All value in a tuple\n")

# writing in over tuple
dementions = (200, 3)
for demention in dementions:
    print(f"Demention in Original {demention}.")

dementions = (400, 100)
for demention in dementions:
    print(f'Demention in Modify {demention}.')
