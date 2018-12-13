#PF-Exer-26

def factorial(number):
    fact=1 #Note: Factorial of zero is 1
    for loopCnt in range(1,number+1):
        fact = loopCnt*fact
    return fact

def find_strong_numbers(num_list):
    strong_num_list=[]
    for num in num_list:
        sum=0
        loop_num=num
        for index in range(0,len(str(loop_num))):
            remainder=loop_num%10
            fact=factorial(remainder)
            loop_num//=10
            sum=sum+fact
        print("sum",sum,"num:",num)
        if(sum==num):
            #print("sum",sum,"loop_num",loop_num,"num:",num)
            strong_num_list.append(num)
    return strong_num_list

num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)