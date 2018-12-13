import re

flight_details="Flight Savana Airlines a2138"

if(re.search(r"Airlines",flight_details)!=None):
    print("Match Found: Airlines")
else:
    print("Match Not Found")

if(re.search(r"a2138$",flight_details)!=None):
    print("Match Found: a2138")
else:
    print("Match Not Found")

if(re.search(r"^F",flight_details)!=None):
    print("Match Found: Message starts with 'F'")
else:
    print("Match Not Found")


if(re.search(r"F..",flight_details)!=None):
    print("Match Found: Word starts with F and two consecutive characters")
else:
    print("Match Not Found")

if(re.search(r"\bSav\b",flight_details)!=None):
    print("Match Found:Word with blank spaces on both sides")
else:
    print("Match Not Found")

if(re.search(r"\d$",flight_details)!=None):
    print("Match Found: Message ends with number")
else:
    print("Match Not Found")

print("Word replaced in the message:")
print(re.sub(r"Flight","Plane",flight_details))
print("Word replaced in the message:")
print(re.sub(r"a(\d{4})",r"A\1",flight_details))


#PF-Tryout
#import re

flight_details="Good Evening, Welcome to British Airways. Your flight number is ba8004. Flight departure time is 16:45"

#This function returns the values in the search result
def printout(search_result):
    if(search_result!=None):
        return search_result.group()
    else:
        return "No Output"

search_result = re.search(r"British Airways",flight_details) #Write your regular expression here for question 1
#This will invoke the printout() and displays the search result values
print(printout(search_result))

search_result = re.search(r"16:45$",flight_details) #Write your regular expression here for question 2
print(printout(search_result))

search_result = re.search(r"Good",flight_details) #Write your regular expression here for question 3
print(printout(search_result))

search_result = re.search(r"Flight",flight_details) #Write your regular expression here for question 4
print(printout(search_result))

print(re.sub(r"ba(\d{4})",r"BA\1",flight_details))