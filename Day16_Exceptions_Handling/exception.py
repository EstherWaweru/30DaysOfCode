#!/bin/python3

import sys


S = input().strip()
#convert it to an integer
try:
    new_s=int(S)
    print(new_s)
except:
    print("Bad String")
