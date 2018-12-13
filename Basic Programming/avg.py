#PF-Exer-30

def find_average(mark_list):
    total=0
    try:
        #print(mark_list)
        for i in range(0,len(mark_list)):
            total+=mark_list[i]
            #print(i)
        marks_avg=total/len(mark_list)
        return marks_avg
    except TypeError:
        print("Type Error Occurred")
    except ValueError:
        print("Value Error Occurred")
    except:
        print("Some error Occurred")

m_list=[1,2,3,4]
print("Average marks:", find_average(m_list))