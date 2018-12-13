import math
g = lambda x,y:x*(x+y)
print(g(8,2))

s = lambda x:math.factorial(x)
print(s(5))

h = lambda x: x >40 and x< 50
print(h(45))

k = lambda x: x>10
if (k(50)):
    print("The number is greater than 10")
else:
    print("The number is less than 10")

m=lambda x,y,z : x+y
print(m(1,2,3)+ g(2,3))

#PF-Exer-38
#This verification is based on string match.
import math
num1=36
num2=10
num3=4

calc = lambda x,y:(x%y)+(x-y) #Write the lambda expression for question1
print(calc(10,4))

square_root = lambda z: math.sqrt(z) #Write the lambda expression for question2
print(square_root(36))

square_root2= lambda b: b**.5 #Write the lambda expression for question3
print(square_root2(49))
                                          