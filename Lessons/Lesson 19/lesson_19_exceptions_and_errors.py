#  List of errors: w3schools.com/python/python_ref_exceptions.asp
# The error for print(x): Traceback (most recent call last):
#   File "C:\Users\tavor\Learning2023Python\Lessons\Lesson 19\lesson_19_exceptions_and_errors.py", line 2, in <module>
#     print(x)
# NameError: name 'x' is not defined

# Handle errors:
x= 2

try:
    # print(x/4.0)
    if not type(x) is str:
        raise TypeError("Only strings are ALLOWED")

except NameError:
    print("NameError means that something is might be undefined, You are Huti!")
except ZeroDivisionError:
    print("ZeroDivisionError means that something is might be divided zero, You are Huti!")
except Exception as error:
    print(error)
else:
    print("No error, you aren't Huti!")
finally:
    print("Im going to print with or without the error, i'm dont know if you are Huti!")