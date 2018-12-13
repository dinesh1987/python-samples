#PF-Tryout
import random
def guess_number(number_in_mind):
    x=1 # remove pass and write your logic here
    y=10
    return(random.randrange(1,10))

#use the print statements given below wherever applicable
#print ('Number is low')
#print ('Number is high')
#print ('You have got it right!!!')

#Provide different values for number_in_mind and test your program
guess_num=4
random_num = guess_number(guess_num)
if(guess_num==random_num):
    print("You have got it right!!!")
elif(guess_num>random_num):
    print("Number is low ")
else:
    print("Number is high ")