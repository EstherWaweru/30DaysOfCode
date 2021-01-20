#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        maximum=[]
        
        
        for a in range(1,n,1):
            for b in range(a+1,n+1,1):
                bitwise=a&b
                if  bitwise<k:
                    maximum.append(bitwise)
                
            
        print(max(maximum))
