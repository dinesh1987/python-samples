observe1="What's happening"
observe2="creating Monkey class"
class Monkey:
    def __init__(self):
        observe4="creating instance vars of that obj."
        self.breed=None
        self.color=None

observe3="creating a Monkey object"
dunston=Monkey()
observe5="dunston refers to that object"
observe6="accessing instance vars through obj. reference"
dunston.breed="Gorilla"
dunston.color="Black"


observe7="creating another Monkey object"
chimpu=Monkey()
observe8="chimpu refers to that object"
observe9="chimpu is a Chimpanzee"
chimpu.breed="Chimpanzee"
observe10="chimpu is Brown in color"
chimpu.color="Brown"


print("Chimpu is a ",chimpu.breed)
print("Dunston is ",dunston.color," in color!!")
#observe1,2,3,4,5,6,7,8,9 and 10 are temporary variables used to explain this concept