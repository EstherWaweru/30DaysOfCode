#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
le=len(a)
counter=0
#buble sort
for i in range(le-1):
    for j in range(0,le-i-1):
        if a[j]>a[j+1]:
            a[j] ,a[j+1] = a[j+1] ,a[j]
            counter+=1
print("Array is sorted in",counter,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[-1])