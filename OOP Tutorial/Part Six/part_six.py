class Employee:
    num_of_emps = 0
    raise_amount = 1.04  # Need to access via the Employee. (the var name) or self. (the var name)

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + "." + last + "@gmail.com"
        Employee.num_of_emps += 1

    # @Property- Like Getter in java etc
    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    # @attr_name- Like Setter in Java etc
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None


emp_1 = Employee("Tavor", "Doron", 50000)
emp_2 = Employee("Test", "User", 30000)
emp_1.first = "taVor"
print(emp_1.email)
print(emp_1.fullname)

emp_2.fullname = "John Doe"
print(emp_2.fullname)

del emp_1.fullname
