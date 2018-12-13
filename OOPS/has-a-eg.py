#OOP-Tryout
                                          
class Address:
    def __init__(self,address_line,city, state):
        self.address_line=address_line;
        self.city=city
        self.state=state

class Clown:
    def __init__(self,name,clown_address):
        self.name=name
        self.__clown_address=clown_address

    def get_clown_address(self):
        return self.__clown_address

#Create the clown object with the given address. Display the name and address of the clown. 
address1=Address("1243,Laughing street","City of Clowns","Jokeland")
clown1=Clown("Mr.Henry",address1)
addr=clown1.get_clown_address()
print("Name: ",clown1.name)
print("Address Line:",addr.address_line)
print("City:",addr.city)
print("State:",addr.state)