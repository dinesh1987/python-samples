class Staff:
    def feed_animal(self,animal,food_quantity):
        if(food_quantity < 5): 
            raise Exception
        elif(food_quantity > 15): 
            raise Exception
        else: 
            print("Feed animal with",food_quantity,"kg of food")

class Monkey:
    pass

class FoodAnchor:
    def send_food(self,animal,staff, food_quantity):
        staff.feed_animal(animal, food_quantity)

    def gossip(self):
        print("Waste time in gossip")

food_anchor=FoodAnchor()
circus_staff=Staff()
chimpu=Monkey()
try:
    food_anchor.send_food(chimpu,circus_staff,2)
    food_anchor.gossip()
except:
    print("Quantity of food sent for the animal is not appropriate!!")