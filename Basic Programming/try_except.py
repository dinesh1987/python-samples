#calculating airport expenditure
def calculate_expenditure(list_of_expenditure):
    total=0
    try:
        for expenditure in list_of_expenditure:
            total+=expenditure
        print(total)
    except:
        print("Some error occured")
        print(total)
    print("Returning back from function.")
    
list_of_values=[100,200,300,"400",500]
calculate_expenditure(list_of_values)