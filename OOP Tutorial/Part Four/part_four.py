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

    def to_string(self):
        return f"first name: {self.first}\nlast name: {self.last}\nsalary: {self.pay} \n"

    # Class methods are methods that changes things for the entire class, for example, the raise_amount
    # Can also be run from the instances
    @classmethod
    def set_raise_amn(cls, amount):
        cls.raise_amount = amount

    # Alternative Constructor
    @classmethod
    def from_string(cls, obj_str):
        first, last, pay = obj_str.split('-')
        return cls(first, last, pay)

    # Static methods-acts like regular methods but connected to the object

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 4 or day.weekday() == 5:  # 4 it's friday 5 it's saturday
            return False
        return True


# Inheritance - Creating Subclasses of the Employee Class
class Developer(Employee):
    raise_amount = 1.10

    # Override __init_ method and Override the to_string method
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def to_string(self):
        return super().to_string() + f"Programing Language {self.prog_lang}\n"


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for i in self.employees:
            print(i.to_string())


emp_1 = Developer("Tavor", "Doron", 50000, "JS")
emp_2 = Developer("Test", "User", 30000, "Python")
mgr_1 = Manager("Sue","Smith",90000,[emp_1])
# print(help(Developer))  # Help on the Developer class
print(isinstance(mgr_1,Manager))
print(isinstance(mgr_1,Employee))
print(isinstance(mgr_1,Developer))
print(issubclass(Developer,Employee))
print(issubclass(Manager,Employee))
print(issubclass(Manager,Developer))
print("\n")

print(mgr_1.to_string())
mgr_1.add_emp(emp_2)
mgr_1.print_emps()

