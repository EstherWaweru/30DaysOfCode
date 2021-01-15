# Enter your code here. Read input from STDIN. Print output to STDOUT
returned_date=input().split()
due_date=input().split()
D1=returned_date[0]
M1=returned_date[1]
Y1=returned_date[2]
D2=due_date[0]
M2=due_date[1]
Y2=due_date[2]
if D1<=D2:
    fine=0
else:
    if Y1>Y2:
        fine=10000
    else:
        if M1<=M2:
            fine=15*(int(D1)-int(D2))
        else:
            fine=500*(int(M1)-int(M2))
print(fine)
    
    
        
        
        

