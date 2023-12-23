# While
value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1

print("\n")
while value <= 10:
    value += 1
    if value == 5:
        continue
    print(value)
else:  # won't show if there is a break
    print("Value is now equal to " + str(value))

print("For Loop ".center(20, "=") + "\n")

names = ["Tavor", "Sara", "John"]
for x in names:
    print(x)

for x in "Mississippi":
    print(x)

for x in names:
    if x == "Sara":
        break
    print(x)

for x in names:
    if x == "Sara":
        continue
    print(x)

# Ranges
for x in range(4):
    print(x)
print("".center(20, "="))
for x in range(2, 4):
    print(x)

print("".center(20, "="))
for x in range(5):
    print(x)

print("".center(20, "="))
for x in range(5, 101, 5):
    print(x)
else:
    print("Glad that\'s over")
print("".center(20, "="))
names = ["Tavor", "Sara", "John"]
actions = ["codes","eats","sleeps"]
for name in names:
    for action in actions:
        print(name+" " + action + ".")


print("".center(20, "="))
for action in actions:
    for name in names:
        print(name+" " + action + ".")