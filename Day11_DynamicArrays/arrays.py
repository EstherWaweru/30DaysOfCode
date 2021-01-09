#!/bin/python3

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

