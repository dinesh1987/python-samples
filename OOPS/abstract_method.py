from abc import ABCMeta, abstractmethod
class CircusAnimal(metaclass=ABCMeta):
    @abstractmethod
    def perform_trick(self):
        print("abstract method invoked")
    def sleep(self,hours):
        print("Sleep for ",hours," hours")

class Monkey(CircusAnimal):
    def perform_trick(self):
        print("Ride Cycle")

class Elephant(CircusAnimal):
    def perform_trick(self):
        print("Dance")

class Lion(CircusAnimal):
    def perform_trick(self):
        print("Jump through rings")

m=Monkey()
e=Elephant()
l=Lion()
#c=CircusAnimal()

list_of_animals=[m,e,l,l,m,m,e]
#print('list_of_animals:',list_of_animals[0:])
for animal in list_of_animals:
    #print('animal:',type(animal))
    animal.perform_trick()
                                                    