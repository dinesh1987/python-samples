#OOP-Tryout
                                      
class Student:
    def __init__(self,student_id,mark1,mark2,mark3):
        self.__student_id=student_id
        self.mark1=mark1
        self.mark2=mark2
        self.mark3=mark3
        self.average_mark=None

    def get_stud_id(self):
        return self.__student_id
    
    def get_average_mark(self):
        return self.average_mark
    
    def calculate_average_mark(self):
        self.average_mark=((self.mark1+self.mark2+self.mark3)/3)

gauti=Student(1001,75,80,85)
gauti.calculate_average_mark()
print("Student Id    :", gauti.get_stud_id())
print("Average Mark  :", gauti.get_average_mark())