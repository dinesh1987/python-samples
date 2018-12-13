#OOP-Exer-5
#Start writing your code here
class Vehicle:
    def __init__(self):
        print("An object has been created for the Vehicle class")
        self.mileage=None
        self.fuel_left=None

    def identify_distance_that_can_be_travelled(self):
        if(self.fuel_left<=5):
            return 0
        else:
            return (self.fuel_left-5)*self.mileage
        
    def identify_distance_travelled(self,initial_fuel):
        #print("self.fuel_left:",self.fuel_left,",initial_fuel:",initial_fuel,",self.mileage",self.mileage)
        return (initial_fuel-self.fuel_left)*self.mileage
    
car=Vehicle()
car.mileage=15
car.fuel_left=8
print("identify_distance_that_can_be_travelled:",car.identify_distance_that_can_be_travelled())
print("identify_distance_travelled:",car.identify_distance_travelled(10))