#OOP-Exer-13
class Juggler:
    def __init__(self,name):
        self.__name=name

    def juggles(self, juggle_item):
        #write the code to make the juggler juggle
        jug_item=JugglingItem(juggle_item)
        #print(self.__name," is juggling with ",juggle_item)
        print(self.__name," is juggling with ",jug_item.get_name())

class JugglingItem:
    def __init__(self,name):
        self.__name=name

    def get_name(self):
        return self.__name
        
jack=Juggler("Jack Bremlov")
anthony=Juggler("Anthony Gatto")
jack.juggles("knives")
anthony.juggles("balls")
#knive=JugglingItem("knives")
#knive=JugglingItem("balls")