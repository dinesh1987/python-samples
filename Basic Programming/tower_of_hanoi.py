def tower_of_hanoi(n, source,destination,temp):
    #print(source)
    if(n==1):
        disk=source.pop(0) #Removes the element in specified position
        destination.insert(0,disk) #Inserts the given element in specified position
        return
    tower_of_hanoi(n-1, source, temp, destination)
    print("-------------------------")
    disk=source.pop(0)
    print("source:",source)
    print("disk:",disk)
    print("temp:",temp)
    print("before:destination:",destination)
    destination.insert(0,disk)
    print("after:destination:",destination)
    tower_of_hanoi(n-1, temp, destination, source)
    return

source=["blue","green","orange"]
destination=[]
temp=[]
tower_of_hanoi(3, source, destination, temp)
print("Source:",source)
print("Destination:",destination)