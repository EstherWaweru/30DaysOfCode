# Enter your code here. Read input from STDIN. Print output to STDOUT
# Objective
# Today we will expand our knowledge of strings, combining it with what we have already learned about loops. Check out the Tutorial tab for learning materials and an instructional video.

# Task
# Given a string,
# , of length that is indexed from to , print its even-indexed and odd-indexed characters as

# space-separated strings on a single line (see the Sample below for more detail).

# Note:

# is considered to be an even index.

# Example

# Print abc def

# Input Format

# The first line contains an integer,
# (the number of test cases).
# Each line of the subsequent lines contain a string,

# .

# Constraints

# Output Format

# For each String
# (where ), print 's even-indexed characters, followed by a space, followed by

# 's odd-indexed characters.

# Sample Input

# 2
# Hacker
# Rank

# Sample Output

# Hce akr
# Rn ak

# Explanation

# Test Case 0:







# The even indices are , , and , and the odd indices are , , and . We then print a single line of space-separated strings; the first string contains the ordered characters from 's even indices (), and the second string contains the ordered characters from 's odd indices (

# ).

# Test Case 1:





# The even indices are and , and the odd indices are and . We then print a single line of space-separated strings; the first string contains the ordered characters from 's even indices (), and the second string contains the ordered characters from 's odd indices ().
#getting an integer input from STDIN you use input() and cast it to a integer using int()
test_cases=int(input())
#looping through the number of test_cases using range(start,stop-1)
for i in range(0,test_cases):
    #getting a string input
    test_strings=input()
    #initializing odd and even list
    evenlist = []
    oddlist = []
    # enumerate a string by returning the index and the character
    for item, char in enumerate(test_strings):
        #check for even items
        if item % 2 == 0:
            evenlist.append(char)
        #check for odd items
        else:
            oddlist.append(char)
    evenstr=''
    oddstr=''
    #converting a list to a string
    evenstr=evenstr.join(evenlist)
    oddstr=oddstr.join(oddlist)
 
    print (evenstr,oddstr)
    
    

