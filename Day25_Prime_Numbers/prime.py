# Enter your code here. Read input from STDIN. Print output to STDOUT
#no of inputs
import math
inputs=int(input())

for j in range(inputs):
    number=int(input())
    
    #getting the various divisors
    if number>1:
        for i in range(2,int(math.sqrt(number))+1):
            if number%i==0:
                print("Not prime")
                break
        else:
            print("Prime")
           
    else:
        print("Not prime")