#!/bin/python3

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