

class Employee:
    def __init__(self,name,salary,emp_id):
        self.name=name
        self.salary=salary
        self.emp_id=emp_id

    def add_bonus(self, amount):
        self.salary += amount


    def is_high_earner(self):
        return self.salary >= 100000

    def display(self):
        high_earner_status = "Yes" if self.is_high_earner() else "No"
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)
        print("High Earner:", high_earner_status)

emp1 = Employee(101, "Lavkush", 95000)
emp1.add_bonus(10000)
emp1.display()