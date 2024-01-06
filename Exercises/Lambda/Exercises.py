

 # One- Write a lambda function to calculate the square of a given number.

task_one = lambda x: x **2
print(task_one(5))

# Task Two- Write a lambda function to check if a given number is even.
task_two = lambda x: x % 2 ==0
print(task_two(5))

# Task Three- Write a lambda function to find the sum of two given numbers.
task_three = lambda x,y : x+y
print(task_three(2,4))

# Task Four- Write a lambda function to extract the first character of a string.
task_four = lambda my_str: my_str[0]
print(task_four('IMRI'))

# Task Five- Write a lambda function to check if a given string is a palindrome.
task_five = lambda my_str: my_str[::-1] == my_str
print(task_five('ABBA'))

# Task Six- Write a lambda function to find the average of a list of numbers.
task_six = lambda list_num: sum(list_num)/len(list_num)
print(task_six([1,2,3,4,5,6]))

# Task Seven- Write a lambda function to extract the domain from an email address (e.g., "user@example.com" should return "example.com").
task_seven = lambda email: email.split('@')[1]
print(task_seven('tavor.doron@gmail.com'))

# Task Eight- Write a lambda function to find the minimum of three numbers.
task_eight = lambda a,b,c: min(a,b,c)
print(task_eight(1,2,3))

# Task Nine- Write a lambda function to check if a given word is a palindrome without considering case (e.g., "level" and "Level" should be considered palindromes).
task_nine = lambda my_str: my_str.lower()[::-1] == my_str.lower()
print(task_nine('Abba'))

# Task ten- Write a function builder that generates a lambda function to calculate the power of a number.
 # The function builder should take an exponent as an argument and return a lambda function that raises a given number to that exponent.

def function_ten(powered_by):
    return lambda num: num ** powered_by

# Examples
by_two= function_ten(2)
print(by_two(5))

# Task Eleven- write a function builder that generates a lambda function to check if a list includes a speciffic value
def function_eleven(val):
    return lambda my_lst: val in my_lst

# Examples
contains_five=function_eleven(5)
print(contains_five([1,2,4,5,"5"]))