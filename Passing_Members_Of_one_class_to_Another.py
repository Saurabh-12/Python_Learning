# An example of pasing members of a class to Another class
class Employee:
    # constructor
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
# Instance method
    def display(self):
        print('Id = ', self.id)
        print('Name = ', self.name)
        print('Salary = ', self.salary)

# Another class display Employee details
class MyClass:
    
    @staticmethod  # Receive Employee class instance
    def myMethod(e):
        e.salary+=1000  # increase the salary by 1000
        e.display()

# Create Emp Object
e = Employee(10, 'Raju',5000.75)
e.display()

print("..........."*5)
# Call static Method of My class and Pass Emp class instance
MyClass.myMethod(e)
