#OOP-Exer-2
#Start writing your code here
class Employee:
    def __init__(self):
        print("An object has been created for employee class")
        self.name=None
        self.age=None
        self.salary=None
        
print("----------------------------------------------------------")
emp1=Employee()
emp1.name="Jack"
emp1.age=24
emp1.salary=30000
print("Name:",emp1.name,",Age:",emp1.age,",Salary:",emp1.salary)

print("----------------------------------------------------------")
emp2=Employee()
emp2.name="Jill"
emp2.age=27
emp2.salary=40000
print("Name:",emp2.name,",Age:",emp2.age,",Salary:",emp2.salary)
