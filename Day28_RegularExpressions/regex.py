#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    set_name=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if re.search(".+@gmail\.com$",emailID):
            set_name.append(firstName)
    # set_name.sort()
    
    for array in sorted(set_name):
        print(array)
