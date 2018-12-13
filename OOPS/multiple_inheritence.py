class Animal:
    def eat(self):
        print("animal eating")
    def sleep(self):
        print("animal sleeping")
class Pet:
    def be_loyal(self):
        print("Pet being loyal")
    def eat(self):
        print("pet eating")

class Dog(Animal,Pet):
    pass
tommy=Dog()
tommy.eat()
tommy.be_loyal()
tommy.sleep()