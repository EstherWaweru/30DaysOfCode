'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
from math import sqrt


# for i in range(1,abs(num1-num2)+1,1):
#     if num1%i==0 and num2%i==0:
#         counter+=1
# print(counter)
#  calculate the greatest common divisor (gcd) of given two numbers, and then count divisors of that gcd. 
def gcd(num1,num2):
    if num1==0:
        return num2
    return gcd(num2%num1,num1)
def commondivisor(num1,num2):
    counter=0
    n=gcd(num1,num2)
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            if n/i==i:
                counter+=1
            else:
                counter+=2
    return counter

if __name__=='__main__':
    # line=input()
    # line=input().split()
    # num1=int(line[0])
    # num2=int(line[1])
    num1=int(input())
    num2=int(input())
    print(gcd(num1,num2))
    print(commondivisor(num1,num2))


