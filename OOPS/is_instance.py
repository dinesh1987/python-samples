class CircusAnimal:
    def eat(self,food):
        print("Eating Food")
    def sleep(self,hours):
        print("Sleep for ",hours," hours")
class Monkey(CircusAnimal):
    def ride_cycle(self):
        print("Ride Cycle")
class Elephant(CircusAnimal):
    def dance(self):
        print("Dance")
class Lion(CircusAnimal):
    def jump_through_rings(self):
        print("Jump through rings")
m=Monkey()
e=Elephant()
l=Lion()        
list_of_animals=[m,e,l,l,m,m,e]
for animal in list_of_animals:
    if isinstance(animal, Monkey):animal.ride_cycle()
    elif isinstance(animal,Elephant):animal.dance()
    else:animal.jump_through_rings()