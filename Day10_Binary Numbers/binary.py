#!/bin/python3
# Objective
# Today, we're working with binary numbers. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given a base-
# integer, , convert it to binary (base-). Then find and print the base- integer denoting the maximum number of consecutive 's in

# 's binary representation. When working with different bases, it is common to show the base as a subscript.

# Example
# The binary representation of is . In base , there are and consecutive ones in two groups. Print the maximum,

# .

# Input Format

# A single integer,

# .

# Constraints

# Output Format

# Print a single base-
# integer that denotes the maximum number of consecutive 's in the binary representation of

# .

# Sample Input 1

# 5

# Sample Output 1

# 1

# Sample Input 2

# 13

# Sample Output 2

# 2

# Explanation

# Sample Case 1:
# The binary representation of
# is , so the maximum number of consecutive 's is

# .

# Sample Case 2:
# The binary representation of
# is , so the maximum number of consecutive 's is .

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
       
        
        
