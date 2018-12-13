class A:
    def __init__(self,value):
        self.__value=value

    def get_value(self):
        return self.__value

class B:
    def __init__(self, var):
        self.__var=var

    def calc(self):
        obj=A(8)
        result=self.__var*obj.get_value()
        return result


b_obj= B(5)
print(b_obj.calc())class A:
    __value=100

    @staticmethod
    def get_value():
        return A.__value

class B:
    def __init__(self, var):
        self.__var=var

    def calc(self):
        result=self.__var*A.get_value()
        return result


b_obj= B(5)
print(b_obj.calc())
                      

                      