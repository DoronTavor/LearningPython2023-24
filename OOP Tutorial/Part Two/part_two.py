# Class Variables - Variables that will have the same value for each instances
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


emp_1 = Employee("Tavor", "Doron", 50000)
emp_2 = Employee("Test", "User", 30000)

Employee.raise_amount = 1.05

emp_1.raise_amount = 1.04 # Only emp_1 will have this value, because we created this value as a instance variable for it
print(emp_1.__dict__)

print(emp_1.raise_amount)
print(Employee.raise_amount)

print(Employee.num_of_emps)
