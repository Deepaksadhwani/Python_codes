from functools import cmp_to_key
import random
class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary  = salary

    def comparator(a, b):
        if a.salary > b.salary:
            return 1
        elif a.salary < b.salary:
            return -1
        else:
            return 0



employees = []

for i in range(5):
    name = f"E{i}"
    salary = random.randint(10000,90000)
    emp = Employee(name,salary)
    employees.append(emp)

sorted_employees = sorted(employees, key=cmp_to_key(Employee.comparator))

print("Employees sorted by salary in descending order:")
for employee in sorted_employees:
    print(f"Name: {employee.name}, Salary: {employee.salary}")
