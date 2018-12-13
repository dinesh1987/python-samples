class CircusAnimal:
    def eat(self,food):
        print("Eat the daily food ",food)
    def sleep(self,hours):
        print("Sleep for ",hours," hours")

class Monkey(CircusAnimal):
    def ride_cycle(self):
        print("Ride cycle")

class Elephant(CircusAnimal):
    def dance(self):
        print("Dance")
    def eat(self,food):
        print("Take Medicine and take ",food)
        #super().eat(food) #Can onvoke both child and parent methods

m=Monkey()
m.eat("Banana!")
m.sleep(7)

e=Elephant()
e.eat("Sugarcane!")
e.sleep(5)