#PF-Exer-41
#This verification is based on string match.

def sum_all(function, data):
    #Remove pass and write the logic here
    sum_of_data=0
    for w in data:
        if(function(w)):
            sum_of_data+=w
    return sum_of_data

list_of_nos=[100,200,300,500,1040]

greater = lambda x: x>10 #Write the lambda expression for question1

divide = lambda x: x%10==0 and x<=100 #Write the lambda expression for question2

range_of_values = lambda x: x>=25 and x<=50 #Write the lambda expression for question3


#Use the below given print statements to display the output
# Also, do not modify them for verification to work
print(sum_all(greater,list_of_nos))
print(sum_all(divide,list_of_nos))
print(sum_all(range_of_values,list_of_nos))