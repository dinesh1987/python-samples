class Cycle:
    def __init__(self,color,brand,cost):
        self.color=color
        self.brand=brand
        self.cost=cost

class Monkey:
    def __init__(self,breed,color,cycle):
        self.breed=breed
        self.color=color
        self.cycle=cycle

cycle1=Cycle("white","Zooko",1500)
cycle2=Cycle("black","Borax",2500)

doodoo=Monkey("Gorilla","black",cycle1)
dunston=Monkey("Chimpu","brown",cycle2)

print(doodoo.cycle.color)
print(doodoo.cycle.cost)
duns_cycle=dunston.cycle
print(duns_cycle.brand)
print(dunston.cycle.brand)
print(dunston.cycle.cost)