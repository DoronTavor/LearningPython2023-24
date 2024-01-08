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


emp_1 = Employee("Tavor", "Doron", 50000)
emp_2 = Employee("Test", "User", 30000)
emp_str_1 = 'John-Doe-70000'
new_emp_3 = Employee.from_string(emp_str_1)
# Check work date
import datetime

my_date = datetime.date(2004, 5, 3)
print(f"Check work day: {my_date} ")
print(Employee.is_work_day(my_date))

print(new_emp_3.to_string())

Employee.set_raise_amn(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
