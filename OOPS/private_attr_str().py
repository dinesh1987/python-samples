class Trainer:
    def __init__(self):
        self.name=None
        self.__salary=1000
    def set_salary(self,salary):
        self.__salary=salary
    def get_salary(self):
        return self.__salary
    def __str__(self):
        return(self.name+" "+(str)(self.__salary))
lion_trainer=Trainer()
lion_trainer.name="Mark"
lion_trainer.set_salary(2000)
print(lion_trainer)