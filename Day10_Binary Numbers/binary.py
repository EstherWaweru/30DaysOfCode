#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    #get the quotient of the n divided by 2
    binary_no=[]
    #using for
    while n>0:
        quotient=n%2
        n=int(n/2)
        
        binary_no.append(quotient)
    #convert a list of numbers to a string 
    binary = ''.join(str(e) for e in binary_no)
    
    #finding the max of the list created
    print(len(max(binary.replace('0',' ').split())))
       
        
        
