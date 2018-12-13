#goal of this tryout is to create a function from scratch and invoke it for the given problem
def convert(input_unit, input_value):
    if(input_unit=='Celsius'):
        return (input_value*(9/5)+32)
    elif(input_unit=='Fahrenheit'):
        return ((input_value-32)*(5/9))
    else:
        return -1

print("37Celsius, in Fahrenheit =",convert("Celsius",37))
print("100Fahrenheit, in Celsius =",convert("Fahrenheit",98))