# String data type
import math

first = "Tavor"
last = "Doron"
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
pizza = str("Olives")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# Concatenation
print("Concatenation \n")
full_name = first + " " + last
print(full_name)
full_name += "!"
print(full_name)

# Casting a number to a string
decade = str(1990)
print(type(decade))
print(decade)

statement = "I like Rock music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
I like Rock music from the 80's
Like Minimal compact 
        Yeah!!!

'''

print(multiline)

# Escaping special characters
sentence = 'I\'m Back! From outer space! \tHey!\n\nWhere\s this at \\ located!'
print(sentence)

# String methods
print("\n\n")
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("l", "c"))
print(multiline)

print(len(multiline))

multiline += "End of the world \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
multiline = "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t" + multiline
print(len(multiline))
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("\n")
# Build a menu
title = "Menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("CheeseCake".ljust(16, ".") + "$4".rjust(4))

# String index value
print("\n")

print(first[1])  # index starts from 0, i Know
print(first[-1])  # The last value in the string
print(first[1:-1])
print(first[1:])

# Some methods return boolean
print(first.startswith("T"))
print(first.endswith("X"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data type
print("\n")

# Int
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float
gpa= 3.28
y= float(1.14)
print(type(gpa))
print(isinstance(y,float))

# Complex type
comp_value= 5+3j
print(comp_value)
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

print(abs(gpa))
print(abs(gpa * -1))
print (round(gpa))
print (round(gpa, 1))
print(math.pi)

# Casting string to number
zipcode="100001"
zip_val= int(zipcode)
print(type(zip_val))