#!/bin/python3

# Objective
# Today, we are building on our knowledge of arrays by adding another dimension. Check out the Tutorial tab for learning materials and an instructional video.

# Context
# Given a
# 2D Array,

# :

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

# We define an hourglass in
# to be a subset of values with indices falling in this pattern in

# 's graphical representation:

# a b c
#   d
# e f g

# There are
# hourglasses in

# , and an hourglass sum is the sum of an hourglass' values.

# Task
# Calculate the hourglass sum for every hourglass in

# , then print the maximum hourglass sum.

# Example

# In the array shown above, the maximum hourglass sum is

# for the hourglass in the top left corner.

# Input Format

# There are
# lines of input, where each line contains space-separated integers that describe the 2D Array

# .

# Constraints

# Output Format

# Print the maximum hourglass sum in

# .

# Sample Input

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0

# Sample Output

# 19

# Explanation

# contains the following hourglasses:

# 1 1 1   1 1 0   1 0 0   0 0 0
#   1       0       0       0
# 1 1 1   1 1 0   1 0 0   0 0 0

# 0 1 0   1 0 0   0 0 0   0 0 0
#   1       1       0       0
# 0 0 2   0 2 4   2 4 4   4 4 0

# 1 1 1   1 1 0   1 0 0   0 0 0
#   0       2       4       4
# 0 0 0   0 0 2   0 2 0   2 0 0

# 0 0 2   0 2 4   2 4 4   4 4 0
#   0       0       2       0
# 0 0 1   0 1 2   1 2 4   2 4 0

# The hourglass with the maximum sum (

# ) is:

# 2 4 4
#   2
# 1 2 4


import math
import os
import random
import re
import sys

def hourglass(arr):
    sum_array=[]
    def shapeofhourglass(arr,row,column):
        a=arr[row-1][column-1]
        b=arr[row-1][column]
        c=arr[row-1][column+1]
        d=arr[row][column]
        e=arr[row+1][column-1]
        f=arr[row+1][column]
        g=arr[row+1][column+1]
        return a+b+c+d+e+f+g
        
    for row in range(1,5):
        for column in range(1,5):
            current_sum=0
            current_sum+=shapeofhourglass(arr,row,column)
            sum_array.append(current_sum)
    print(max(sum_array))
            
            

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    hourglass(arr)

