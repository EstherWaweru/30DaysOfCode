# Enter your code here. Read input from STDIN. Print output to STDOUT

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
    
    

