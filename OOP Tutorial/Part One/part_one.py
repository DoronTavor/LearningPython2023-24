class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@gmail.com"

    def fullname(self):
        return f"{self.first} {self.last}"



emp_1 = Employee("Tavor", "Doron", 50000)
emp_2 = Employee("Test", "User", 30000)

print(emp_1.email)
print(emp_1.fullname())
print(emp_2.fullname())

# Can run like this
print(Employee.fullname(emp_1))
