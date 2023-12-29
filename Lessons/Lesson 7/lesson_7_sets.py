# Sets
nums = {1, 2, 3, 4}
nums2 = set((1, 2, 3, 4))
print(nums)
print(nums2)
print(type(nums))
print(type(nums2))
print(len(nums))

# No Duplicate are allowed

nums = {1, 2, 2, 3}
print(nums)  # Don't print the duplicate and don't brings an error

# True is a duplicate of 1, and False is a duplicate of 0
nums = {1, True, 2, False, 3, 4, 0}  # Prints the first of the duplicates
print(nums)

# Check if a value is in a set
print(2 in nums)

# but you cannot refer to an element in the set with the index position or key

# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
more_nums = {5, 6, 7}
nums.update(more_nums)
print(nums)

# you can use update with lists, tuples and dictionaries too.

# Merge two sets to create a new one
one = {1, 2, 3}
two = {5, 6, 7}
my_new_set= one.union(two)
print(my_new_set)

# keep only duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)

# keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
