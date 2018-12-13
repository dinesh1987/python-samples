my_list=[0]*5
print(my_list)
for index in range(1,len(my_list)):
    my_list[index]=(index-1)*10
    #print(my_list)
    print((index-1)*10)
print(my_list)