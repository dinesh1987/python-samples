#Normal functions
Q=[1,3,4,5,6,7,8,9,10,15,20]

def sum_all():
    total=0
    for i in Q:
        total=total+i
    print(total)

def sum_even():
    total=0
    for i in Q:
        if(i%2==0):
            total=total+i
    print(total)

def sum_divisibleby3():
    total=0
    for i in Q:
        if(i%3==0):
            total=total+i
    print(total)

sum_all()
sum_even()
sum_divisibleby3()

#Higher order and lambda functions
def sum_all(function, data):
    result_sum=0;
    for w in data:
        if(function(w)):
            result_sum = result_sum+ w
    return result_sum

Q=[1,3,4,5,6,7,8,9,10,15,20]

p = lambda x:x

q = lambda x : x%2 == 0

r = lambda x : x%3 == 0

print(sum_all(p,Q))
print(sum_all(q,Q))
print(sum_all(r,Q))