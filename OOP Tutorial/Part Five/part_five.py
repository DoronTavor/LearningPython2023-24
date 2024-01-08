# In this Python Object-Oriented Tutorial, we will be learning about special methods. These are also called magic or dunder methods.
# These methods allow us to emulate built-in types or implement operator overloading. These can be extremely powerful if used correctly.
class Employee:
    num_of_emps = 0
    raise_amount = 1.04  # Need to access via the Employee. (the var name) or self. (the var name)

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"
        Employee.num_of_emps += 1

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __repr__(self):
        return f"Employee ({self.first}, {self.last}, {self.pay})"

    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee("Tavor", "Doron", 50000)
emp_2 = Employee("Test", "User", 30000)
print(emp_1)

print(repr(emp_1))  # equal to emp_1.__repr__()
print(emp_1+emp_2) # equal to emp1.__add__(emp_2)
print(len(emp_1))