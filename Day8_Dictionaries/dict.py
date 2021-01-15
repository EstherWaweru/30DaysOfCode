# Enter your code here. Read input from STDIN. Print output to STDOUT
#getting the number of entries
n=int(input())
phoneBook={}

for i in range(n):
    #get an input string
    sample_str=input().split()
    
    phoneBook[sample_str[0]]=sample_str[1]
    # phoneBook=dict([(sample_lst[0],sample_lst[1])])
    # print(phoneBook)
    
for i in range(n):
    #get the value of the keys
    try:
        sample_key=str(input().strip())
        #check if the key exist
        if phoneBook.get(sample_key)!=None:
            #concatenate the strings
            print(sample_key+'='+phoneBook[sample_key])
        else:
            print("Not found") 
    except:
        break
   
