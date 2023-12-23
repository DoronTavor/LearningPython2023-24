# Dictionaries
# Like JS Objects

band = {
    'vocals': 'Plant',
    'guitar': 'Page'
}

band_two = dict(vocals='Plant', guitar='Page')

print(band)
print(band_two)
print(band == band_two)
print(type(band))
print(len(band))

# Access items

print(band["vocals"])
print(band.get("guitar"))

# List all keys
print(band.keys())

# List all values
print(band.values())

# List of key-value pairs as tuples
print(band.items())

# Check if key exists
print("guitar" in band)
print("triangle" in band)

# Change values
band['vocals'] = 'Coverdale'
print(band)
band.update({'bass': 'JPJ'})
print(band)

# Remove items
print(band.pop("bass"))
print(band)

# Add value

band["drums"] = "Bonham"
print(band)

# Remove the last added
print(band.popitem())  # Tuple
print(band)

# Delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band_two.clear()
print(band_two)

del band_two
# Can't print it after that

# Copy Dictionaries

# band_two = band  # creates a reference
# print( " Bad copy !")
# print(band_two)
# band_two['drums'] = "Dave"
# print(band)

band_two = band.copy()
band_two['drums'] = "Dave"
print(" Good Copy ")
print(band)
print(band_two)

# or use the dict() constructor function
band_three = dict(band)
print("Good Copy")
print(band_three)

# Nested Dictionaries
member1 = {
    'name': 'Plant',
    'instrument': 'vocals'
}
member2 = {
    'name': 'Page',
    'instrument': 'guitar'
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]['name'])

