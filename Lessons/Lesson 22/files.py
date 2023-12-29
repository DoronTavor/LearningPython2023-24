
import os
f = open("names.txt")
# print(f.read())
# print(f.read(4))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()  # it's important to close the file

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file doesn't exist")
finally:
    f.close()

# Append- create the file if it doesn't exist
f = open("names.txt","a")
f.write("\nNeil")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)
f = open("context.txt","w")
f.write("\nI deleted all of the context")
f.close()
f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file
f = open("name_list.txt","w")
f.close()

# Creates the specified file but returns an error if the file exists
if not os.path.exists("tavor.txt"):
    f = open("tavor.txt","x")
    f.close()

# Delete a file
# avoid an error if it doesn't exist
if os.path.exists("name_list.txt"):
    os.remove("name_list.txt")
else:
    print("The file doesn't exist")
