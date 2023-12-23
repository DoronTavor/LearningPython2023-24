users = ["Tavor", "John", "Sara"]

data = ["Tavor", 19, True]

print("Tavor" in users)

print(users[0])
print(users[-1])  # Last value in list
print(users[-2])

print(users.index("Sara"))
print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append("Elsa")
print(users)

users += ["Jason"]  # must use the [] because if not, every letter will be in different index
print(users)
users.extend(["Robert", "Jimmy"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

# replace value and delete
users[1:3] = ["Robert", "JPJ"]
print(users)

users.remove("Bob")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

# Sort
users[1:2] = ["dave"]  # When it's lowercase, it stands after all the words with uppercase
users.sort()
print(users)

# Alphabetical Sort
users.sort(key=str.lower)
print(users)

# Numbers
nums = [4, 42, 78, 1, 5]
nums.reverse() # Not by the sizes of the numbers
print(nums)

# nums.sort(reverse=True) # Descending
# print(nums)

print(sorted(nums,reverse=True)) # Not change the original list
print(nums)

nums_copy = nums.copy()
my_nums = list(nums)
my_copy = nums[:]
print(my_nums)
my_copy.sort()
print(my_copy)
print(nums_copy)

print(type(nums))
