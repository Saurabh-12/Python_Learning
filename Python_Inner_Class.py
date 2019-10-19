# class inside class 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def displayDetails(self):
        print("Name = ", self.name+" Age = ", self.age)

# Inner class
    class Dob:
        def __init__(self):
            self.dd = 10
            self.mm = 5
            self.yy = 1989
        def displayDob(self):
            print("Dob = {}/{}/{}".format(self.dd,self.mm,self.yy))


# Creating Person class Object
p = Person("Raju",23)
p.displayDetails()

# Creating Inner class object
inner = Person("Raju",23).Dob()
inner.displayDob()
print(inner.yy)
 
        

        
        