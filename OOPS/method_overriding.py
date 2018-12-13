class CircusAnimal:
    def eat(self,food):
        print("Eating Food")
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

list_of_animals=[m,e,l,l,m,m,e]

for animal in list_of_animals:
    animal.perform_trick()