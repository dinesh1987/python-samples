try:
    flight_file=open("flight.txt","r")
    text=flight_file.read()
    print(text)
    flight_file.write(",Good Morning")   
except:
    print("Error occurred")
finally:        
    print("File is being closed")
    flight_file.close()
    if flight_file.closed:
        print("File is closed")
    else:
        print("File is open")