class CircusAnimal:
    def wave_after_performance(self,counter):
        wave_counter = 0
        while(wave_counter < counter):
            print("waving after performance")
            wave_counter+=1
    def bow_before_performance(self):
        print("Bowing before performance")

class Monkey(CircusAnimal):
    def ride_cycle(self):
        self.bow_before_performance()
        print("Riding cycle")
        self.wave_after_performance(3)

class Elephant(CircusAnimal):
    def dance(self):
        self.bow_before_performance()
        print("Dancing")
        self.wave_after_performance(4)

class Lion(CircusAnimal):
    def jump_through_ring(self):
        self.bow_before_performance()
        print("Jumping through rings")
        self.wave_after_performance(2)

print("Monkey's performance:")
dunston=Monkey()
dunston.ride_cycle()