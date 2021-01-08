# Enter your code here. Read input from STDIN. Print output to STDOUT
#getting the number of entries
n=int(input())
phoneBook={}

for i in range(n):
    #get an input string
    sample_str=input().strip()
    #convert the string to a list
    sample_lst=list(sample_str.split())
    #create a dictionary
    
    phoneBook[sample_lst[0]]=sample_lst[1]
    # phoneBook=dict([(sample_lst[0],sample_lst[1])])
    # print(phoneBook)
    
for i in range(n):
    #get the value of the keys
    sample_key=str(input().strip())
    #check if the key exist
    if phoneBook.get(sample_key)!=None:
        #concatenate the strings
        print(sample_key+'='+phoneBook[sample_key])
    else:
        print("Not found") 
   
