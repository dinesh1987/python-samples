
class LessFoodException(Exception):
    def __init__(self,food_quantity):
        message="Food given was "+str(food_quantity)+"kg. Increase the food given to the animal"
        super().__init__(message)

class MoreFoodException(Exception):
    def __init__(self,food_quantity):
        message="Food given was "+str(food_quantity)+"kg. Decrease the food given to the animal"
        super().__init__(message)

class Staff:
    def feed_animal(self,animal,food_quantity):
        if(food_quantity< 5): 
            raise LessFoodException(food_quantity)
        elif(food_quantity> 15): 
            raise MoreFoodException(food_quantity)
        else: 
            print("Fed animal with",food_quantity,"kg of food")

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
except LessFoodException as e:
    print(e)
except MoreFoodException as e:
    print(e)
except Exception as e:
    print("Some error occurred.")