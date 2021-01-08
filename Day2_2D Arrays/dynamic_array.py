#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    #finding the shape of the hour glass
    # abc
    #  d
    # efg
    def hour_glass(arr,row,col):
        a=arr[row-1][col-1]
        b=arr[row-1][col]
        c=arr[row-1][col+1]
        d=arr[row][col]
        e=arr[row+1][col-1]
        f=arr[row+1][col]
        g=arr[row+1][col+1]
        hour_sum=0
        hour_sum+=a+b+c+d+e+f+g
        return hour_sum
#remove the first and last rows and column of the array
    sum_list=[]
    for row in range(1,5):
        for col in range(1,5):
            current_sum=hour_glass(arr,row,col)
            sum_list.append(current_sum)
    return max(sum_list)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
