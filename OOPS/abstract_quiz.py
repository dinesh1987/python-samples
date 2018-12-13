from abc import ABCMeta, abstractmethod
class Parent(metaclass=ABCMeta):
    def __init__(self): 
        self.num=5
    @abstractmethod
    def show(self):
        pass
    
class Child(Parent):  
    def __init__(self):
        super().__init__()
        self.var=10
 
class GrandChild(Child):
    def show(self):
        print(self.num)
        print(self.var)
        print("This is possible") 
        
obj=GrandChild()  
obj.show()