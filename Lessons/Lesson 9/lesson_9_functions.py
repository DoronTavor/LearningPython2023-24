def hello_world():
    print("Hello World!")


hello_world()


def sum(num1=0, num2=0):
    if type(num1) is not int or type(num2) is not int:
        return 0
    return num1 + num2


total = sum(2, 3)
print(total)
print(sum("a", 5))
print(sum())


def multuple_items(*args):
    print(args)
    print(type(args))


multuple_items("Dave", "Tavor", "John")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first_name="Tavor", last_name="Doron")