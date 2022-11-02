
# without function 
"""
a=int(input())
b=int(input())
if a==1:
    for number in range (a+1, b+ 1):
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            print(number)
if a!=1:
    for number in range (a, b+ 1):
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            # cause of error is if a==1 it will consider 1 as a prime number :) change it 
            #if a==1:
                #print(number-[0]
            #else:
            print(number)
"""
# with function
def is_prime(num):
    if num == 1:return 0
    for i in range(2, num):
        if num % i == 0:return 0
    return 1

a = int(input())
b = int(input())
for i in range(a, b+1):
    if is_prime(i) == 1:
        print(i)