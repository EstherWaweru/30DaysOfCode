#!/bin/python3
# Objective
# Today, we will learn about the Array data structure. Check out the Tutorial tab for learning materials and an instructional video.

# Task
# Given an array,
# , of integers, print

# 's elements in reverse order as a single line of space-separated numbers.

# Example

# Print 4 3 2 1. Each integer is separated by one space.

# Input Format

# The first line contains an integer,
# (the size of our array).
# The second line contains space-separated integers that describe array

# 's elements.

# Constraints

# Constraints

# , where is the

#     integer in the array.

# Output Format

# Print the elements of array

# in reverse order as a single line of space-separated numbers.

# Sample Input

# 4
# 1 4 3 2

# Sample Output

# 2 3 4 1

import math
import os
import random
import re
import sys


#REversing an array.Here are some techniques of doing it
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))\
    #slicing
    reversed_array=arr[::-1]
    for i in range(len(reversed_array)):
        print(reversed_array[i],end=' ')
    #inbuilt reverse method
    # print(arr.reverse())
    #built in reversed function and then casting it to list
    #print(list(reversed(arr)))