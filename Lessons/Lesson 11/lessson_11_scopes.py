name = "Tavor"  # Global scope- can be read in functions but can't be changed
# print(name)
count = 1


def another():
    def greeting(first_name):
        print(first_name)
        print(name)
        global count
        count += 1
        print(count)
        color = "Blue"  # Isn't defined in the global scope
        print(color)

    greeting("Tavor")


another()
