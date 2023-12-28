squared = lambda num: num * num

print(squared(2))

addTwo = lambda num: num + 2
print(addTwo(12))

sum = lambda a, b: a + b
print(sum(3, 3))


############ Uses of Lambda #########

def func_builder(x):
    return lambda num: num + x


add_ten = func_builder(10) # Creating a function
add_twenty = func_builder(20)

print(add_ten(7))
print(add_twenty(7))