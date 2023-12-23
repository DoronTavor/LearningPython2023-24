# Tuples
# Like list, but the order of the data wont change and the values wont change

my_tuple = tuple(("Tavor", 19, True))
another_tuple = (1, 4, 2, 8)
print(my_tuple)
print(type(my_tuple))
print(another_tuple)
print(type(another_tuple))

# Everything we learned in list can be used in tuple

new_list = list(my_tuple)
new_list.append("Neil")
new_tuple = tuple(new_list)
print(new_tuple)

(one, two, *hey) = another_tuple
print(one)
print(two)
print(hey)  # holds the remain
