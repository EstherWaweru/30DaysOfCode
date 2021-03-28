# A left rotation operation on an array shifts each of the array's elements unit to the left. For example, if left rotations are performed on array , then the array would become

# . Note that the lowest index item moves to the highest index in a rotation. This is called a circular array.

# Given an array
# of integers and a number, , perform

# left rotations on the array. Return the updated array to be printed as a single line of space-separated integers.

# Function Description

# Complete the function rotLeft in the editor below.

# rotLeft has the following parameter(s):

#     int a[n]: the array to rotate
#     int d: the number of rotations

# Returns

#     int a'[n]: the rotated array

# Input Format

# The first line contains two space-separated integers
# and , the size of and the number of left rotations.
# The second line contains space-separated integers, each an

# .

# Constraints

# Sample Input

# 5 4
# 1 2 3 4 5

# Sample Output

# 5 1 2 3 4

# Explanation

# When we perform

# left rotations, the array undergoes the following sequence of changes:



#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    #rotate array by d elements speed O(n)
    n=len(a)
    print("Lenght of a",n)
    temp=[]
    i=0
    while(i<d):
        temp.append(a[i])
        i+=1
    i=0
    while(d<n):
        a[i]=a[d]
        d+=1
        i+=1
    a[:]=a[:i]+temp
    # leftrotate(a,d)
    # slice(a,d)
    return a
        
#rotate all elements O(n*d)
def leftrotate(a,d):
    for i in range(d):
        leftrotation(a,d)
def leftrotation(a,d):
    temp=a[0]
    n=len(a)
    for i in range(n-1):
        a[i]=a[i+1]
    a[n-1]=temp
#slicing
def slice(a,d):
    
    a[:]=a[d:n]+a[:d]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
