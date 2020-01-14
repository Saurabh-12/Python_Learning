# @classmethod vs @staticmethod vs "plain" methods
# What's the difference?

class MyClass:
    def method(self):
        """
        Instance methods need a class instance and
        can access the instance through `self`.
        """
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        """
        Class methods don't need a class instance.
        They can't access the instance (self) but
        they have access to the class itself via `cls`.
        """
        return 'class method called', cls

    @staticmethod
    def staticmethod():
        """
        Static methods don't have access to `cls` or `self`.
        They work like regular functions but belong to
        the class's namespace.
        """
        return 'static method called'

# All methods types can be
# called on a class instance:
obj = MyClass()
print(obj.method())  # O/P:- ('instance method called', <MyClass instance at 0x1019381b8>)
print(obj.classmethod()) # O/P:- ('class method called', <class MyClass at 0x101a2f4c8>)
print(obj.staticmethod()) # O/P:- 'static method called'

# Calling instance methods fails
# if we only have the class object:
print(MyClass.classmethod()) # O/P:- ('class method called', <class MyClass at 0x101a2f4c8>)
print(MyClass.staticmethod()) # O/p:- 'static method called'
# MyClass.method() 
'''
TypeError: 
    unbound method method() must be called with MyClass
    instance as first argument (got nothing instead)
    '''