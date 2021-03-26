# loop through the array and count elements whose value=0

def countzeroes(A):
    counter=0
    for i in range(len(A)):
        if A[i]==0:
            counter+=1
    return (counter)
    

if __name__=='__main__':

    lst=[1,0,5,0,6,2]
    print(countzeroes(lst))

