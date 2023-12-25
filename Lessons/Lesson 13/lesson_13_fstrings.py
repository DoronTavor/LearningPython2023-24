person = "Tavor"
coins = 3
print("\n" + person + " has " + str(coins) + " coins left.")

# Examples

message = "\n%s has  %s coins left. " % (person, coins)
print(message)

# Newer method

message = "\n{} has {} coins left. ".format(person, coins)

print(message)

message = "\n{1} has {0} coins left. ".format(coins, person)

print(message)

message = "\n{person} has {coins} coins left. ".format(coins=coins, person=person)

print(message)

player = {'person': 'Tavor', 'coins': 3}
message = "\n{person} has {coins} coins left. ".format(**player)

print(message)

################
# f-Strings! This is the way.

message = f"\n{person} has {coins} coins left"
print(message)

message = f"\n{person} has {2*5} coins left"
print(message)

message = f"\n{person.upper()} has {2*5} coins left"
print(message)

message = f"\n{player['person']} has {player['coins']**2} coins left"
print(message)

# Passing formatting options

num = 10
print(f"\n2.25 {num} is {2.25*num :.2f}.")
