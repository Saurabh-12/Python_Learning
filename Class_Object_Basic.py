# Class and object basic concept
# An object does not exist without a class, however a class can exist without any object.
class MyClass:
    objCount = 0  # Class or static variable
    
    @staticmethod  # Static Method
    def displayCount():
        print ("Total Obj count %d" % MyClass.objCount)
        
    # This is constructore 
    def __init__(self, id,name):
        MyClass.objCount +=1
        self.id = id
        self.name = name  # instance variable

    # Instance method
    def display(self):
        print(self.id)
        print(self.name)

# calling the method by object Raju
raju = MyClass(10, "Raju")
raju.display()
MyClass.displayCount()  # Calling static Method by Class name

print("-------"*5)
# Object Shyam
shyam = MyClass(11, "Shyam")
shyam.display()
MyClass.displayCount()

print("-------"*5)
# Object Raghu
shyam = MyClass(12, "Raghu")
shyam.display()
MyClass.displayCount()

''' Understanding Class method '''
print("-------"*5)
class Bird:
    wings = 2  # class variable
    
    @classmethod
    def fly(cls, name):
        print("{} flies with {} wings ".format(name,cls.wings))

Bird.fly('Sparrow')
Bird.fly('Pigeon')
     
        
    