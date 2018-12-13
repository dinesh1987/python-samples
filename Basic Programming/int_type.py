#calculating airport expenditure
def calculate_expenditure(list_of_expenditure):
    total=0
    for expenditure in list_of_expenditure:
        if(type(expenditure) is int):
            total+=expenditure
        else:
            print("Wrong data type")
            break
    print(total)

list_of_values=[100,200,300,"400",500]
calculate_expenditure(list_of_values)